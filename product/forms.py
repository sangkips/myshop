from django import forms
from . models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']