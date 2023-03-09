from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import datetime, timedelta

# Create your models here.
class Sector(models.Model):

    sectors = [
        ('Bank', 'Bank'),
        ('NGO', 'NGO'),
        ('Finance', 'Finance'),
        ('Education', 'Education'),
        ('Hospitality', 'Hospitality'),
        ('IT', 'IT'),
        ('Engineering', 'Engineering'),
        ('Transportation', 'Transportation'),
        ('Legal-Service', 'Legal Service'),
        ('Health', 'Health'),
        ('Manufacturing', 'Manufacturing'),
        ('Creative-Art', 'Creative Art'),
        ('Skill-Work','Skill Work'),
    ]
    name = models.CharField(max_length=20, choices=sectors, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Sectors'


    
class Company(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=300)
    address = models.CharField(
        max_length=200
    )
    website = models.CharField(
        max_length=100, 
        blank=True,
        null=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    short_description = RichTextField(
        null=True, 
        blank=True, 
        verbose_name='Short Description'
    )
    logo = models.ImageField(
        upload_to='images/',
        default="images/default.jpg"
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):

        self.slug = slugify(f'{self.name} {str(datetime.now())}') 
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

    regions = [
        ('Addis-Ababa', 'Addis Ababa'),
        ('Dre-Dawa', 'Dre Dawa'),
        ('Afar', 'Afar'),
        ('Amhara', 'Amhara'),
        ('Tigray', 'Tigray'),
        ('Benishangul-Gumuz', 'Benishangul Gumuz'),
        ('Gambela', 'Gambela'),
        ('Harari', 'Harari'),
        ('Oromia', 'Oromia'),
        ('Sidama', 'Sidama'),
        ('Somali', 'Somali'),
        ('SNNPR','SNNPR'),
        ('SWEP','SWEP'),
        ('Unspecified','Unspecified'),
    ]

    

    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sectors  = models.ManyToManyField(Sector)

    description = RichTextField()
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=300)
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
 
    region = models.CharField(
        max_length=20,
        choices=regions
    )
    quantity_required = models.IntegerField(
        verbose_name='Quanity Required',
        null=True,
        blank=True
    )
    how_to_apply = RichTextField(
        verbose_name='How To Apply'
    )
    deadline = models.DateField()

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title} {str(datetime.now())}') 
        super(Job, self).save(*args, **kwargs)

    def isNew(self):
        createdAt = datetime(self.created_at.year, self.created_at.month, self.created_at.day)
        return createdAt > datetime.today() - timedelta(days=5)
    def has_expired(self):
        deadline = datetime(self.deadline.year, self.deadline.month, self.deadline.day)
        return datetime.today() > deadline
    def assigned_sectors(self):
        return ', '.join([sector.name for sector in self.sectors.all()])


class ContactMessage(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)
    message = models.TextField(verbose_name="Message", max_length=500)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class PageViews(models.Model):
    page = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    visit = models.IntegerField()

    def __str__(self):
        return self.page

    class Meta:
        verbose_name_plural = 'Page Views'

