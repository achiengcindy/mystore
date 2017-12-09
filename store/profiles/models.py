from django.db import models
from django.conf import settings

class profile(models.Model):
	name = models.CharField(max_length=120)
	user = models.
	description = models.TextField()
	location = models.CharField(max_length=120,default='my location', blank=True, null=True)
	job = models.CharField(max_length=120, null=True)
	
	def __str__(self):
		return self.name