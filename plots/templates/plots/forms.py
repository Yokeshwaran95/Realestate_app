from django import forms

class NameForm(forms.Form):
	uname=forms.CharField(label='your_name', max_length=100)