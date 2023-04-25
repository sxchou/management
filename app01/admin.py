from django.contrib import admin
from app01 import models
# Register your models here.
admin.site.register(models.City)
admin.site.register(models.Order)
admin.site.register(models.UserInfo)
