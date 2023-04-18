from django.contrib import admin
from mystaticinfo.models import MyStaticInfo

class StaticInfoAdmin(admin.ModelAdmin):
    list_display = ['my_off_no', 'my_off_email', 'my_off_address', 'my_cv']

admin.site.register(MyStaticInfo, StaticInfoAdmin);
# Register your models here.
