from django.contrib import admin
from . import models
# Register your models here.

# class CompanyAdmin(admin.ModelAdmin):


admin.site.register(models.Company)
admin.site.register(models.Job)