from django import forms
from captcha.fields import CaptchaField

class UserRegistrationForm(forms.Form):
    phone_number = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()