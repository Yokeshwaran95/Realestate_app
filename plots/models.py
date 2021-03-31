from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL

sale_type=(("Rent","Rent"),
	("Sale","Sale"),
	("Lease","Lease"),
	)
# Create your models here.

class Name(models.Model):
	name=models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Properties(models.Model):
	title=models.CharField(max_length=500,blank=False,null=False,default="No Title property")
	Name=models.ForeignKey(User,on_delete=models.CASCADE,related_name="property",default=1)
	location=models.CharField(max_length=500, blank=False, null=False)
	description=models.TextField()
	contact_num=models.CharField(max_length=10, blank=False, null=False)
	Price=models.IntegerField(default=1)
	Type=models.CharField(max_length=30)
	sale_type=models.CharField(max_length=30,choices=sale_type,default="Rent")
	posted_on=models.DateTimeField(auto_now=True)
	updated_on=models.DateTimeField(auto_now_add=True)
	title_slug=models.SlugField(default=' ')


	def __str__(self):
		return self.location
