from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from . models import Profile
class userRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_image',]

class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']