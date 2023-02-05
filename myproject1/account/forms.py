from django import forms
from django.contrib.auth.models import User

class_attrs = {'class': "form__input"}


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs=class_attrs),
        error_messages={'required': 'Username is required'}
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(attrs=class_attrs),
        error_messages={'required': 'Password is required'}
    )


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)
        labels = {
            "email": "Email"
        }
        help_texts = {
            "username": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            "email": "Required"
        }
        widgets = {
            'username': forms.TextInput(attrs=class_attrs),
            'first_name': forms.TextInput(attrs=class_attrs),
            'last_name': forms.TextInput(attrs=class_attrs),
            'email': forms.EmailInput(attrs={'class': 'form__input', 'required': 'class'}),
            'password': forms.PasswordInput(attrs=class_attrs),
        }
