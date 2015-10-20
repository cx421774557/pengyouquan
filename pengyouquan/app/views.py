from django.shortcuts import render
from django.http import HttpResponse
import json

import sys

from models import UserInfo

# Create your views here.

def index(request):
	user_list = UserInfo.objects.exclude(name = '').order_by('-friendscount')[:6]
	data_dict = {}
	n = 1
	for user in user_list:
		data_dict[n] = {}
		data_dict[n]['uid'] = user.uid
		data_dict[n]['name'] = user.name
		n = n + 1
	context_dict = {'user_list': user_list, 'data_dict' : json.dumps(data_dict)}
	return render(request, 'app/index.html', context_dict)

def About(request):
	return HttpResponse("app says here is the about page!")

def GetUserinfo(request):
	_uid = request.GET['uid']
	userinfo_dict = GetTree(_uid, 3)
	return HttpResponse(json.dumps(userinfo_dict), content_type = 'application/json')

def GetTree(uid, leave):
	if leave > 0:
		json_dict  = Getinfo(uid)
		friendslist = json_dict['friendslist'].split(',')
		if len(friendslist) > 0 and leave > 1:
			json_dict['children'] = []
			for friend in friendslist:
				json_dict['children'].append(GetTree(friend, leave - 1))
		return json_dict

def Getinfo(uid):
	try:
		user = UserInfo.objects.get(uid = uid)	
	except:
		print "can't find user uid:" + uid 
		pass
	else:
		json_dict = {
			'id': user.id,
			'uid':user.uid,
			'name' :  user.name,
			'isStar': user.isStar,
			'friendscount' : user.friendscount,
			'friendslist' : user.friendslist,
			'views' : user.views,
			'region' : user.region,
			'subcount' : user.subcount,
			'pubcount' : user.pubcount,
		}
		return json_dict
	