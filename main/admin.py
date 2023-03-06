from django.contrib import admin
from . import models
# Register your models here.

# class CompanyAdmin(admin.ModelAdmin):

class CompanyAdmin(admin.ModelAdmin):
    exclude = ['slug']

class JobAdmin(admin.ModelAdmin):
    exclude = ['slug']

admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Job, JobAdmin)