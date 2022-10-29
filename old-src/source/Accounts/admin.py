from django.contrib import admin
from .models import UserInfo, User
# Register your models here.
admin.site.register(User)
admin.site.register(UserInfo)