from django.db import models

# Create your models here.

#during uploading filename doesn't change on using this function
def upload_location(instance,filename):
	return "%s%s" %(instance.id,filename)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=upload_location)
    uploaded_at = models.DateTimeField(auto_now_add=True)

