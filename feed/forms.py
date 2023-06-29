from django.contrib.auth.forms import UserCreationForm
from .models import User
#from forms import CustomUserForm
from .models import * 

from django import forms

class CustomUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    Password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password1'}))
    Password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password2 '}))
    class Meta:
        model=User 
        fields=['username','email','password1','password2']
