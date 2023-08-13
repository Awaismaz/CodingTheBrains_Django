from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Profile

def my_email_validator(email):
    if email.split('@')[1].split('.')[0].lower() == 'hotmail':
        raise ValidationError("Email Not Acceptable")


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator(),my_email_validator])
    verify_email = forms.CharField()
    message=forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        cleaned_data['email'] = cleaned_data.get('email').lower()
        cleaned_data['verify_email'] = cleaned_data.get('verify_email').lower()
        message = cleaned_data.get('message')

        if cleaned_data.get('email') != cleaned_data.get('verify_email'):
            raise forms.ValidationError("Email Mismatch")
        
        return cleaned_data
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        # fields = ['name','age','gender']
        # exclude = ['name','age','gender']

