from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Ex.: João Silva'
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro =forms.CharField(
        label='Nome de cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Ex.: João Silva'
            }
        )
    )
    email=forms.EmailField(
        label='email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Ex.: joaosilva@xpto.com'
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Digite sua senha'
            }
        )
    )
    senha_2=forms.CharField(
        label='Confirme sua Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Digite sua senha novamente'
            }
        )
    )

#precisa comecar com o 'clean_' e depois o nome do campo
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        #verifica se o nome existe
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('não é possível inserir espaços dentro do nome de cadastro')
            else:
                return nome
        
    
    def clean_senha_2(self):
         senha_1 = self.cleaned_data.get('senha_1')
         senha_2 = self.cleaned_data.get('senha_2')

        #verifica se elas existem
         if senha_1 and senha_2:
           if senha_1 != senha_2:
               raise forms.ValidationError('Senhas diferentes')
           else:
               return senha_2