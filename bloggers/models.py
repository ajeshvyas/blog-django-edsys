from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=250)
	desc = models.CharField(max_length=5000)
	img = models.ImageField()
	author = models.CharField(max_length=50)
	upload_datetime = models.DateTimeField(auto_now_add=True)