from django.contrib import admin
from Abouts.models import About
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ['about_key','about_value']

admin.site.register(About, AboutAdmin);
