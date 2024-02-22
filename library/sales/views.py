from django.shortcuts import render
from django import forms
from allauth.account.forms import UserChangeForm
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'phone_number', 'profile_picture')

# Create your views here.
