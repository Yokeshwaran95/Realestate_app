
from django.contrib import admin
from django.urls import path
from plots.views import ( intro, contact, PlotsView, PostView, PropertiesDetailView, PropertiesDeleteView)
from plots.views import registration
from django.views.generic import ( CreateView,TemplateView )
from django.contrib.auth.views import (LoginView,PasswordResetView)
from plots.models import Properties
from plots.forms import PostForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name="Home"),
    path('login/',LoginView.as_view(),name="login"),
    path('forgot-password/',PasswordResetView.as_view(),name="password_reset"),
    path('contact/',contact,name="contact"),
    path('plots/',PlotsView.as_view(),name="plots"),
    path('create/',PostView.as_view(),name="post"),
    path('register/',registration,name="signup"),
    path('plots/<pk>/',PropertiesDetailView.as_view(),name="detail"),
    path('<pk>/delete/',PropertiesDeleteView.as_view(),name="delete"),
    path('register/',registration.as_view(),name="signup")

]
