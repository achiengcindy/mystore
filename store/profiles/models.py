from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up


class profile(models.Model):
	name = models.CharField(max_length=120)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
	description = models.TextField()
	location = models.CharField(max_length=120,default='my location', blank=True, null=True)
	job = models.CharField(max_length=120, null=True)
	
	def __str__(self):
		return self.name

class userStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=208,null=True, blank=True)


	def __str__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else:
			return self.user.username

			
		
