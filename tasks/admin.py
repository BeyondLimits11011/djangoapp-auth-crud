from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readojnly_fileds = ("created",)

# Register your models here.
admin.site.register(Task, TaskAdmin)