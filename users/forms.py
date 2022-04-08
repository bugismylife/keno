from django import forms
from .models  import NewUser
class LoginForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ['email', 'password',]
        labels = {
            "email": "",
            "password": ""
        }

        widgets = {
            "email": forms.TextInput(attrs={
                'class': 'form-control input-lg',
                'style': 'max-width: 100%;',
                'placeholder': 'Email'
                }
            ),
            "password": forms.PasswordInput(attrs={
                'class': 'form-control input-lg', 
                'style': 'max-width: 100%;',
                'placeholder': 'Şifre'
                }
            )
        }
