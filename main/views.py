from django.shortcuts import render, get_object_or_404
from .models import Company, Job
from django.http import HttpRequest
from datetime import datetime, timedelta
from django.http import HttpRequest
from django.db.models import Q
from operator import and_
from functools import reduce


# Create your views here.

def home(request):
    today = datetime.today() 
    jobs = Job.objects.filter(created_at__range = [today,  today + timedelta(days=5)])[:4]
    context = {
        "isHomeActive": True,
        "jobs": jobs
    }
    return render(request, 'pages/home.html', context)

def jobs(request:HttpRequest, page = 0):
    workModesOriginal =["On-site", "Remote", "Hybrid"]
    jobTypesOriginal = [
        'Contract', 
        'Full-time',
        'Part-time',
        'Internship',
        'Volunteer',
        'Temporary',
        'Other'
    ]
    experiencesOriginal = [
        'Entry Level',
        'Junior Level',
        'Mid Level',
        'Senior Level', 
        'Managerial Level', 
        'Executive',
        'Senior Executive'
    ]
    sectorsOriginal  = [
        'Bank', 
        'NGO',
        'Finance', 
        'Education', 
        'Hospotality', 
        'IT',
        'Engineering', 
        'Transportation', 
        'Legal-Service' 
        'Health', 
        'Manufacturing', 
        'Creative-Art',
        'Skill-Work Work'
    ]
    regionsOriginal = [
        'Addis-Ababa', 
        'Dre-Dawa', 
        'Afar', 
        'Amhara', 
        'Tigray', 
        'Benishangul-Gumuz',
        'Gambela', 
        'Harari', 
        'Oromia', 
        'Sidama', 
        'Somali', 
        'SNNPR',
        'SWEP',
        'Unspecified',
    ]
    workModes = request.GET.getlist("work_mode")
    jobTypes = request.GET.getlist("employement_type")
    experiences = request.GET.getlist("experience")
    sectors = request.GET.getlist("sector")
    regions = request.GET.getlist("region")
    searchQuery = request.GET.get('search')

    startIndex = page * 10
    endIndex = startIndex + 10
    total = Job.objects.filter(
        job_type__in=jobTypes if len(jobTypes) > 0 else jobTypesOriginal,
        work_mode__in=workModes if len(workModes) > 0 else workModesOriginal,
        experience__in=experiences if len(experiences) > 0 else experiencesOriginal,
        sector__in=sectors if len(sectors) > 0 else sectorsOriginal,
        region__in=regions if len(regions) > 0 else regionsOriginal,
        title__icontains = searchQuery if searchQuery else ""
    ).count()
    jobs = Job.objects.all().filter(
        job_type__in=jobTypes if len(jobTypes) > 0 else jobTypesOriginal,
        work_mode__in=workModes if len(workModes) > 0 else workModesOriginal,
        experience__in=experiences if len(experiences) > 0 else experiencesOriginal,
        sector__in=sectors if len(sectors) > 0 else sectorsOriginal,
        region__in=regions if len(regions) > 0 else regionsOriginal,
        title__icontains = searchQuery if searchQuery else ""
    )[startIndex:endIndex]
    numOfPages = int(total / 10)
    nextPage = page
    prevPage = page
    if(page + 1 <= numOfPages):
        nextPage = page + 1
    if(page - 1 >= 0):
        prevPage = page - 1

    context = {
        "jobs": jobs,
        "isJobsActive":True,
        "currentPage": page,
        "numOfPages": numOfPages,
        "nextPage": nextPage,
        "prevPage": prevPage,
        "total": total,
        "workModes": workModes,
        "jobTypes": jobTypes,
        "experiences": experiences,
        "sectors": sectors,
        "regions": regions
    }

    return render(request, 'pages/jobs.html', context)

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug) 
    relatedJobs = Job.objects.filter(sector = job.sector).exclude(slug = slug)[:4]

    context = {
        'slug': slug,
        "job": job,
        "relatedJobs": relatedJobs
    }
    return render(request, 'pages/job-detail.html', context)

def companies(request:HttpRequest, page = 0):
    startIndex = page * 10
    endIndex = startIndex + 10
    total = Company.objects.count()
    companies = Company.objects.all()[startIndex:endIndex]
    numOfPages = int(total / 10)
    nextPage = page
    prevPage = page
    if(page + 1 <= numOfPages):
        nextPage = page + 1
    if(page - 1 >= 0):
        prevPage = page - 1

    context = {
        "companies": companies,
        "isCompaniesActive":True,
        "currentPage": page,
        "numOfPages": numOfPages,
        "nextPage": nextPage,
        "prevPage": prevPage,
        "total": total
    }
    return render(request, 'pages/companies.html', context)

def company_detail(request, slug, page = 0 ):
    company = get_object_or_404(Company, slug=slug) 
    jobs = company.job_set.all()
    startIndex = page * 10
    endIndex = startIndex + 10
    total = company.job_set.count()
    filteredJobs = jobs[startIndex:endIndex]
    numOfPages = int(total / 10)
    nextPage = page
    prevPage = page
    if(page + 1 <= numOfPages):
        nextPage = page + 1
    if(page - 1 >= 0):
        prevPage = page - 1

    context = {
        'slug': slug,
        'jobs': filteredJobs,
        'company': company,
        "currentPage": page,
        "numOfPages": numOfPages,
        "nextPage": nextPage,
        "prevPage": prevPage,
        "total": total
    }

    return render(request, 'pages/company-detail.html', context)