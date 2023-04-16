from django.contrib import admin
from home.models import home

class HomeAdmin(admin.ModelAdmin):
    list_display=['home_desc', 'long_desc']

admin.site.register(home, HomeAdmin);

# Register your models here.
