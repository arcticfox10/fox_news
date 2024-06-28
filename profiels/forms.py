import email
from tkinter import Widget
from django import forms
from django.contrib.auth import get_user_model



User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField( widget=forms.PasswordInput)
  

       
    
