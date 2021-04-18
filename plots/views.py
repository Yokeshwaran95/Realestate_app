from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from plots.models import ( Profile, Properties )
from plots.forms import ( NameForm, SignUpForm )
from django.views.generic import ( ListView, CreateView, DetailView, DeleteView )
from django.contrib.auth.mixins import ( LoginRequiredMixin )
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password


# Create your views here.

def intro(request):
	return render(request,"index.html")

# def contact(request):
# 	# print(request.POST)
# 	if request.method=="POST":
# 		form=NameForm(request.POST)
# 		if form.is_valid():
# 			name=form.cleaned_data['uname']
# 			N=Name(name=name)
# 			N.save()
# 			return render(request,"contact.html",{'form': form})
# 	return render(request,"contact.html")

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/register.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()


    return render(request, 'registration/register.html', {'form': form})



# class Registration(CreateView):
#   template_name = 'registration/register.html'
#   success_url = reverse_lazy('login')
#   form_class = RegisterForm


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
	fields=['title','location','description','contact_num','Price','sale_type','Type','Img']
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
