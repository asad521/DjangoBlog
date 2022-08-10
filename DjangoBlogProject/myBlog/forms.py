from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Blogpost
from django.utils.translation import gettext,gettext_lazy as _
#  Overriding Inherit UserCreationFrom, OV password and Adding User model  
class SingupForm(UserCreationForm):
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        labels = {'username':'User Name','first_name':'First Name','last_name':'Last Name','email':'Email',}
        
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'})}
        
        
        
#  Overriding Inherit AuthenticationForm, OV Username   
class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'autfocus': True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title','desc']
        labels = {"desc":"Description","title":"Title"}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'desc':forms.Textarea(attrs={'class':'form-control'})}
        