from django.db import models

# Create your models here.
class User(models.Model):
	id = models.IntegerField(primary_key=True)
	password = models.CharField(max_length=150)
	name = models.CharField(max_length=64)
	usertype = models.IntegerField()
	username = models.CharField(max_length=64)
	factory = models.CharField(max_length=60)