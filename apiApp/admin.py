from django.contrib import admin
from .models import Plan

class MyPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product']

admin.site.register(Plan, MyPlanAdmin)
