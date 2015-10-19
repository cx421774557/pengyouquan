from django.db import models
#from django.template.defaultfilters import  slugily
from django.contrib.auth.models import User


# Create your models here.

class pubUserAttr(models.Model):

	name = models.CharField(max_length=128, unique=True)
	pubcount = models.IntegerField(default=0)
	uid = models.IntegerField(default=0)
	profileinfo = models.CharField(max_length=128, unique=True)
	authinfo = models.CharField(max_length=128, unique=True)
	subby = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name


class subUserAttr(models.Model):
	name = models.CharField(max_length=128, unique=True)
	subcount = models.IntegerField(default=0)
	uid = models.IntegerField(default=0)
	profileinfo = models.CharField(max_length=128, unique=True)
	subto = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name


class UserInfo(models.Model):
	
	uid = models.IntegerField(unique=True)
	name = models.CharField(max_length=128)
	isStar = models.IntegerField(default = 0)
	friendscount = models.IntegerField(default = 0)
	friendslist = models.CharField(max_length = 128)
	views = models.IntegerField(default = 0)
	region = models.CharField(max_length = 128)
	subcount = models.IntegerField(default=0)
	pubcount = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name