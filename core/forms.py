from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholer': 'Your username',
        'class': 'w-full py-4 px-6 roundex-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholer': 'Your password',
        'class': 'w-full py-4 px-6 roundex-xl'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholer': 'Your username',
        'class': 'w-full py-4 px-6 roundex-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholer': 'Your email address',
        'class': 'w-full py-4 px-6 roundex-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholer': 'Your password',
        'class': 'w-full py-4 px-6 roundex-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholer': 'Repeat password',
        'class': 'w-full py-4 px-6 roundex-xl'
    }))