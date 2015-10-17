import json
import time

#import yaml

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pengyouquan.settings')

import django
django.setup()

from app.models import pubUserAttr, subUserAttr, UserInfo

def list2str(list):
	_str = ''
	for x in list:
		_str = _str + str(x) + ','
	return _str

def populate():
	sum_dict = {}
	with open('media/summary.txt', 'r') as f:
		useinfo = f.readline()
		sum_dict = json.loads(useinfo)
		for k, v in sum_dict.items():
			uid = int(k, 10)
			name = ''
			friendscount = 0
			friendslist = ''
			views = 0
			isStar = 0
			region = ''
			subcount = 0
			pubcount = 0

			if 'name' in v.keys():
				name = v['name']
			if 'friends_cnt' in v.keys():
				friendscount = v['friends_cnt']
			if 'views' in v.keys():
				views = v['views']
			if 'sub_cnt' in v.keys():
				subcount = v['sub_cnt']
			if 'pub_cnt' in v.keys():
				pubcount = v['pub_cnt']
			if 'region' in v.keys():	
				region = v['region']
			if 'is_star' in v.keys():
				isStar = v['is_star']
			if 'friends_list' in v.keys():
				friendslist = list2str(v['friends_list'])[:-1]
			add_useinfo(uid, name, friendscount, friendslist, views, region, isStar, subcount, pubcount)
			


def add_useinfo(uid, name, friendscount, friendslist, views, region, isStar, subcount, pubcount):
	u = UserInfo.objects.get_or_create(
		uid = uid,
		name = name,
		friendscount = friendscount,
		friendslist = friendslist,
		views = views,
		region = region,
		isStar = isStar,
		subcount = subcount,
		pubcount = pubcount
		)[0]
	return u

if __name__ == '__main__':
	populate()