from django.contrib import admin
from . import models
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    exclude = ['slug']

class JobAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'company', 'sector', 'hasExpired' ]
    list_filter = ['sector']
    exclude = ['slug']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name', 'email', 'created_at' ]

    def has_add_permission(self, request, obj=None):
        return False

class PageViewsAdmin(admin.ModelAdmin):
    list_display = [ 'page', 'created_at', 'visit' ]
    def has_add_permission(self, request, obj=None):
        return False
    
admin.site.site_header = 'Corporate Ethiopia'

admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Job, JobAdmin)
admin.site.register(models.ContactMessage, ContactMessageAdmin)
admin.site.register(models.PageViews,PageViewsAdmin )