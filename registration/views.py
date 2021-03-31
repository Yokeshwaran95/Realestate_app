from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from plots.models import ( Name, Properties )
from plots.forms import NameForm, RegisterForm
from django.views.generic import ( ListView, CreateView, DetailView, DeleteView )
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def registration(request):
	print(request.POST)
	if request.method=="POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/login")
	else:
		form=RegisterForm()
	return render(request,"registration/register.html",{'form': form})



