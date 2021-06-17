
from django.contrib import admin
from django.urls import path
from plots.views import ( intro, PlotsView, PostView, PropertiesDetailView, PropertiesDeleteView, signup, contact)
from django.views.generic import ( CreateView,TemplateView )
from django.contrib.auth.views import (LoginView,PasswordResetView)
from plots.models import Properties
from plots.forms import PostForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name="Home"),
    path('login/',LoginView.as_view(),name="login"),
    path('forgot-password/',PasswordResetView.as_view(),name="password_reset"),
    path('contact/',contact,name="contact"),
    path('plots/',PlotsView.as_view(),name="plots"),
    path('create/',PostView.as_view(),name="post"),
    path('plots/<pk>/',PropertiesDetailView.as_view(),name="detail"),
    path('<pk>/delete/',PropertiesDeleteView.as_view(),name="delete"),
    path('register/',signup,name="signup")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)