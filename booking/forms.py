# forms.py
from django import forms

class PasswordResetForm(forms.Form):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
