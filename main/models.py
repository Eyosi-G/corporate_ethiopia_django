from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.
class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


    
class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(
        max_length=100, 
        blank=True,
        null=True
    )
    slug = models.SlugField(unique=True)
    email = models.EmailField(
        blank=True, 
        null=True
    )
    short_description = RichTextField(
        max_length=400, 
        null=True, 
        blank=True, 
        verbose_name='Short Description'
    )
    logo = models.ImageField(
        upload_to='uploads/',
        null=True, 
        blank=True
    )
    header_image = models.ImageField(
        upload_to='uploads/', 
        null=True,
        blank=True,
        verbose_name='Header Image'
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

        
    class Meta:
        verbose_name_plural = 'Companies'


class Job(models.Model):
    experiences = [
        ('Entry Level', 'Entry Level'),
        ('Junior Level', 'Junior Level'),
        ('Mid Level', 'Mid Level'),
        ('Senior Level', 'Senior Level'),
        ('Managerial Level', 'Managerial Level'),
        ('Executive', 'Executive'),
        ('Senior Executive', 'Senior Executive')
    ]
    jobTypes = [
        ('Contract', 'Contract'),
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Volunteer', 'Volunteer'),
        ('Temporary', 'Temporary'),
        ('Other', 'Other'),
    ]
    workModes = [
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
    ]
    title = models.CharField(max_length=100)
    description = RichTextField()
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    experience = models.CharField(
        choices=experiences,
          max_length=20,
         verbose_name='Experience'
    )
    job_type = models.CharField(
        choices=jobTypes,
        max_length=20, 
        verbose_name='Job Type'
    )
    work_mode = models.CharField(
        choices=workModes,
        max_length=20,
        verbose_name='Work Mode'
    )
    quantity_required = models.IntegerField(
        verbose_name='Quanity Required',
        null=True,
        blank=True
    )
    how_to_apply = models.TextField(
        max_length=200,
        verbose_name='How To Apply'
    )
    deadline = models.DateField()

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
