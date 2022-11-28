from django.contrib import admin
# import models over from models.py
from . import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'approved', 'created_on',)


admin.site.register(models.Recipe)

