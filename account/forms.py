from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'details'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'details'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'details'}))
    

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')
        widgets = {
        'username':forms.TextInput(attrs= {'class':'details'}),
        'last_name':forms.TextInput(attrs= {'class':'details'}),
        'first_name':forms.TextInput(attrs= {'class':'details'}),   
        } 