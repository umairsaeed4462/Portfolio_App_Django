from django.contrib import admin
from contactinquery.models import ContactInquery

class ContactInqueryAdmin(admin.ModelAdmin):
    list_display=['user_name', 'user_email', 'user_project', 'user_message']

admin.site.register(ContactInquery, ContactInqueryAdmin);
# Register your models here.