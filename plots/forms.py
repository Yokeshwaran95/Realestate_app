from django import forms
from plots.models import Properties
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NameForm(forms.Form):
	uname=forms.CharField(label='your_name', max_length=100)

class PostForm(forms.ModelForm):
	class Meta:
		model=Properties
		fields='__all__'

class RegisterForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=["username", "email", "password1", "password2"]




