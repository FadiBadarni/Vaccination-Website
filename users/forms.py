from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()   # email field addition

    class Meta:      # nested namespace for configs
        model = User   # model to be affected
        fields = ['username', 'email', 'password1', 'password2']   # fields in order


class DoctorRegisterForm(ModelForm):
    username = models.CharField(max_length=100)
    email = forms.EmailField()
    password = models.CharField(max_length=100)

    class Meta:      # nested namespace for configs
        model = User   # model to be affected
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'email', 'password']  # fields in order


