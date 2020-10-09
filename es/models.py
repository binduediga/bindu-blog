from django.db import models
class EMAIL(models.Model):
	username=models.CharField(max_length=20)
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	Email=models.EmailField(max_length=50)
	img=models.ImageField(upload_to='attachments/',null=True)
	