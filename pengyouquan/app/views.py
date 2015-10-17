from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	dict_r = {"key":"hello"}
	return render(request, 'app/index.html', dict_r)

def About(request):
	return HttpResponse("app says here is the about page!")