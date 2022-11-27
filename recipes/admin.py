from django.contrib import admin
# import models over from models.py
from . import models
# Register your models here.
admin.site.register(models.Recipe)
admin.site.register(models.Comment)
