from django import forms
from plots.models import Properties
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=["username", "email", "password1", "password2"]




