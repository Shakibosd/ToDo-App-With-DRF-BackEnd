from django.contrib import admin
from .models import Plan
from django.utils.html import format_html

class MyPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product']

admin.site.register(Plan, MyPlanAdmin)
