from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ("created",)
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),

            "subject": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'subject'
            }),

            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),

            "message": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text message'
            })
        }
