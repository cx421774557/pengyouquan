from django.db import models
#from django.template.defaultfilters import  slugily
from django.contrib.auth.models import User


# Create your models here.

class pubUserAttr(models.Model):

	name = models.CharField(max_length=128, unique=True)
	pubcount = models.IntegerField(default=0)
	Id = models.IntegerField(default=0)
	profileinfo = models.CharField(max_length=128, unique=True)
	authinfo = models.CharField(max_length=128, unique=True)
	subby = models.IntegerField(default=0)


class subUserAttr(models.Model):

	name = models.CharField(max_length=128, unique=True)
	subcount = models.IntegerField(default=0)
	Id = models.IntegerField(default=0)
	profileinfo = models.CharField(max_length=128, unique=True)
	subto = models.IntegerField(default=0)



class UserInfo(models.Model):
	Id = models.IntegerField(default=0)
	name = models.CharField(max_length=128, unique=True)
	isStar = models.CharField(max_length=128, unique=True)
	birthday = models.CharField(max_length=128, unique=True)
	location = models.CharField(max_length=255, unique=True)
	subcount = models.IntegerField(default=0)
	pubcount = models.IntegerField(default=0)