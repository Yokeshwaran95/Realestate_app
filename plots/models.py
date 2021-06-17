from django.db import models
from django.conf import settings
# from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import ( post_save,pre_save )
from django.dispatch import receiver
from plots.utils import unique_slug_generator


sale_type=(("Rent","Rent"),
	("Sale","Sale"),
	("Lease","Lease"),
	)
# Create your models here.


#Email validator
def check_gmail(value):
	if "@gmail.com" in value:
		return value
	else:
		raise ValidationError("This field accepts only gmail")

# class Profile(models.Model):
# 	name=models.OneToOneField(User, on_delete=models.CASCADE)
# 	email=models.EmailField(max_length=100,validators=[check_gmail],default="abc@gmail.com")
# 	password1=models.CharField(max_length=14,default="******")
# 	bio = models.TextField(max_length=500, blank=True)
# 	location = models.CharField(max_length=30, blank=True)
# 	birth_date = models.DateField(null=True, blank=True)

# 	def __str__(self):
# 		return self.name
# 	@receiver(post_save, sender=User)
# 	def update_user_profile(sender, instance, created, **kwargs):
# 	    if created:
# 	        Profile.objects.create(user=instance)
# 	    instance.profile.save()

class Properties(models.Model):
	title=models.CharField(max_length=500,blank=False,null=False,default="No Title property")
	# Name=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="property",default=1)
	location=models.CharField(max_length=500, blank=False, null=False)
	description=models.TextField()
	contact_num=models.CharField(max_length=10, blank=False, null=False)
	Price=models.IntegerField(default=1)
	Type=models.CharField(max_length=30)
	sale_type=models.CharField(max_length=30,choices=sale_type,default="Rent")
	posted_on=models.DateTimeField(auto_now=True)
	updated_on=models.DateTimeField(auto_now_add=True)
	slug=models.SlugField(max_length=255)
	Img=models.ImageField(upload_to="images/", default=None)

	def __str__(self):
		return self.location

	def get_description(self):
		return self.description.split(',')

def rl_pre_save_receiver(sender,instance, *args, **kwargs):
	print('saving...')
	print(instance.posted_on)
	if not instance.slug:
		instance.slug=unique_slug_generator(instance)

def rl_post_save_receiver(sender,instance, *args, **kwargs):
	print('saved...')
	print(instance.posted_on)


pre_save.connect(rl_pre_save_receiver, sender=Properties)