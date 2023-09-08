from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # https://stackoverflow.com/questions/62502854/css-not-working-on-django-password-form-field
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'input'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class': 'input'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name' : TextInput(attrs={'class': 'input'}),
            'username' : TextInput(attrs={'class': 'input'}),
            'email' : EmailInput(attrs={'class': 'input'}),
        }
      