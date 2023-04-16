from django.contrib import admin
from userauth.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'logo']

admin.site.register(User, UserAdmin);