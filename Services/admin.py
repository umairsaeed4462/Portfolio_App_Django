from django.contrib import admin
from Services.models import Services
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['ser_icon', 'ser_title', 'ser_desc']

admin.site.register(Services, ServicesAdmin);