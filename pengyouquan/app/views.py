from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return HttpResponse("app says hello !")

def About(request):
	
	return HttpResponse("app says here is the about page!")