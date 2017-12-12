from django.db import models
from django.utils import timezone


#during uploading filename doesn't change on using this function
def upload_location(instance,filename):
	return "%s%s" %(instance.id,filename)

class Post(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title =models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date =models.DateTimeField(blank=True, null=True)
	image=models.ImageField(upload_to=upload_location,
		null=True,blank=True, width_field='width_field',height_field='height_field')
	width_field=models.IntegerField(default=100)
	height_field=models.IntegerField(default=200)
	#image=models.FileField(null=True,blank=True)
	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title





