from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from plots.models import ( Name, Properties )
from plots.forms import NameForm, RegisterForm
from django.views.generic import ( ListView, CreateView, DetailView, DeleteView )
from django.contrib.auth.mixins import ( LoginRequiredMixin )
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


# Create your views here.

def intro(request):
	return render(request,"index.html")

def contact(request):
	# print(request.POST)
	if request.method=="POST":
		form=NameForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['uname']
			N=Name(name=name)
			N.save()
			return render(request,"contact.html",{'form': form})
	return render(request,"contact.html")

# def registration(request):
# 	print(request.POST)
# 	if request.method=="POST":
# 		form=RegisterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect("/login")
# 	else:
# 		form=RegisterForm()
# 	return render(request,"registration/register.html",{'form': form})



class registration(SuccessMessageMixin, CreateView):
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')
  form_class = RegisterForm
  success_message = "Your profile was created successfully"


class PropertiesDetailView(DetailView):
	template_name="detail.html"
	model=Properties

class PropertiesDeleteView(DeleteView):
	template_name="Delete.html"
	model=Properties
	def get_success_url(self):
		return reverse("plots")


class PostView(LoginRequiredMixin,CreateView):
	model=Properties
	fields=['title','location','description','contact_num','Price','sale_type','Type']
	login_url="/login/"
	def get_success_url(self):
		return reverse("Home")

class PlotsView(ListView):
	model=Properties
	template_name='plots.html'
	def get_queryset(self,*args,**kwargs):
		qs=super(PlotsView,self).get_queryset(*args,**kwargs)
		qs=qs.order_by('posted_on')
		return qs
