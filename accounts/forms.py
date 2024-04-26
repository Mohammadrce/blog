from django import forms
from django.contrib.auth.models import User
from django.forms.utils import ValidationError


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label="username")
    email = forms.EmailField(widget=forms.EmailInput(), label='email')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label='password_confirm')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            raise ValidationError("Password is not match!")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label='password')

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data


class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
