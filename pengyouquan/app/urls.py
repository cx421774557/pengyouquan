from django.conf.urls import patterns, url, include
from app import views

urlpatterns = patterns(' ',
	url(r'^$', views.index, name = 'index'),
	url(r'^about/$', views.About, name = 'About'),
	url(r'^getuserinfo/$', views.GetUserinfo, name = 'Getuserinfo'),
)