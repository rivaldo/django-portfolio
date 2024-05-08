from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def login(request):
    form = LoginForms()
    
    print('passou 01')
    print(request.method)
    
    if request.method == 'POST':
        
        form = LoginForms(request.POST)
        
        print('passou 02')
        
        if form.is_valid():
            print('FORM VALID')
            nome = form['nome_usuario'].value()
            senha = form['senha'].value()
            print(nome, senha)
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )
        print(usuario)
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, usuario)
            return redirect('login')
        
    return render(request, 'usuarios/login.html', {'form':form})
#################################################################################################################################
def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            if form['senha'].value() != form['confirma_senha'].value():
                return redirect('cadastro')
            nome = form['nome_usuario'].value()
            email = form['email'].value()
            senha = form['senha'].value()
            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')