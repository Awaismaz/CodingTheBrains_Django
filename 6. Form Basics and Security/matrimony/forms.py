from django import forms

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email = forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
    

        

