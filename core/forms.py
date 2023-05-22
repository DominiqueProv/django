from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    inputClass = 'w-full p-3 mb-2 rounded-xl'

    username = forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Your username',
      'class': inputClass
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
      'placeholder': 'Your password',
      'class': inputClass
    }))


class SignupForm(UserCreationForm):
    inputClass = 'w-full p-3 mb-2 rounded-xl'

    username = forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Your username',
      'class': inputClass
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
      'placeholder': 'Your email address',
      'class': inputClass
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
      'placeholder': 'Your password',
      'class': inputClass
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
      'placeholder': 'Repeat password',
      'class': inputClass
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        