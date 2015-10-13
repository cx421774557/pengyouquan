from django.contrib import admin
from app.models import UserInfo
from app.models import subUserAttr
from app.models import pubUserAttr

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(subUserAttr)
admin.site.register(pubUserAttr)
