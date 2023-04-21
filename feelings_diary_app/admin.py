from django.contrib import admin

from .models import Teacher, DiaryEntry

# Register your models here.

admin.site.register(Teacher)
admin.site.register(DiaryEntry)