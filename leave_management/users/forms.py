from django import forms
from .models import User
import re

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        if not re.match(r'^(?=.*[A-Z])(?=.*\d).{8,}$', password):
            raise forms.ValidationError("Password must be 8+ chars, with 1 uppercase & 1 digit")
        return cleaned_data
