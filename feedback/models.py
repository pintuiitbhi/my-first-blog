from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	#CHOICES=[('select1','select 1'),('select2','select 2')]
	#describe=models.TextField()
	#short=models.CharField(max_length=200)
	#select=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	user = models.OneToOneField(User,unique=False,default='ax10',on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	phone= models.CharField(max_length=10, blank=True)
	address = models.CharField(max_length=1024,null=True)
	age = models.PositiveIntegerField(blank=True,null=True)
	
	gender = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)		