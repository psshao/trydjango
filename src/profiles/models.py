from django.db import models
from django.conf import settings

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length = 1200)
	description = models.TextField(default = 'default description')


	def __unicode__(self):
		return self.name