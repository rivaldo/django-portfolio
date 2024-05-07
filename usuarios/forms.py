from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "type":"text",
                "class":"form-control",
                "name":"nome_login", 
                "placeholder":"Ex.: Rivaldo"
                
            }
        )
    )
    
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "name":"password", 
                "placeholder":"Digite sua senha, por favor"
            }
        )
    )

class CadastroForms(forms.Form):
    
    nome_usuario = forms.CharField(
        label='Nome do Cadastro',
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
            "class":"form-control", 
            "name":"nome_cadastro", 
            'placeholder':'Ex.: Rivaldo',
            }
        )
    )
    
    email = forms.EmailField(
        label='Endereço de e-mail',
        required=True,
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'class':"form-control",
                'name':"email", 
                'placeholder':"Ex.: joaosilva@xpto.com"
            }
        )
    )
    
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "name":"password",
                "placeholder":"Digite sua senha"
            }
        )
    )
    confirma_senha = forms.CharField(
        label='Confirme a Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "name":"confirma_password",
                "placeholder":"Confirme a sua senha"
            }
        )
    )