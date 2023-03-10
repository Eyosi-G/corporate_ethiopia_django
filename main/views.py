from django.shortcuts import render, get_object_or_404
from .models import Company, Job, ContactMessage, PageViews,Sector
from django.http import HttpRequest
from datetime import datetime, timedelta
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def incrementView(request):
    url = request.path_info
    today = datetime.today() 
    try:
        pageView = PageViews.objects.get(created_at=today, page=url)
        pageView.visit += 1
        pageView.save()
    except PageViews.DoesNotExist:
        PageViews.objects.create(page=url, visit=1)

def sendEmailBack(form):
    firstName = form.cleaned_data["first_name"]
    lastName = form.cleaned_data["last_name"]
    email = form.cleaned_data["email"]
    message = form.cleaned_data["message"]
    ContactMessage.objects.create(
        first_name = firstName,
        last_name = lastName,
        email = email,
        message = message
    )
   

def home(request:HttpRequest):
    incrementView(request)
    today = datetime.today() 
    year = datetime.now().year
    url = request.path_info
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sendEmailBack(form)
            messages.success(request, 'Thanks !! Your message is successfully submitted. We will contact you soon.')
            return HttpResponseRedirect(url)


    jobs = Job.objects.filter(created_at__range = [today - timedelta(days=5), today])[:4]
    context = {
        "isHomeActive": True,
        "jobs": jobs,
        "form": form,
        "url": url,
        "year": year
    }
    return render(request, 'pages/home.html', context)

def jobs(request:HttpRequest ):
    incrementView(request)
    year = datetime.now().year
    url = request.path_info
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sendEmailBack(form)
            messages.success(request, 'Thanks !! Your message is successfully submitted. We will contact you soon.')
            return HttpResponseRedirect(url)
    page = 0
    if request.method == "GET" and request.GET.get("page"):
        page = int(request.GET.get("page"))

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
        'Senior Level', 
        'Managerial Level', 
        'Executive',
        'Senior Executive'
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
    allSectors = Sector.objects.all()
    filterSectors = Sector.objects.filter(name__in=sectors)
    total = Job.objects.filter(
        job_type__in=jobTypes if len(jobTypes) > 0 else jobTypesOriginal,
        work_mode__in=workModes if len(workModes) > 0 else workModesOriginal,
        experience__in=experiences if len(experiences) > 0 else experiencesOriginal,
        sectors__in=filterSectors if len(filterSectors) > 0 else allSectors,
        region__in=regions if len(regions) > 0 else regionsOriginal,
        title__icontains = searchQuery if searchQuery else ""
    ).distinct().count()
    jobs = Job.objects.all().filter(
        job_type__in=jobTypes if len(jobTypes) > 0 else jobTypesOriginal,
        work_mode__in=workModes if len(workModes) > 0 else workModesOriginal,
        experience__in=experiences if len(experiences) > 0 else experiencesOriginal,
        sectors__in=filterSectors if len(filterSectors) > 0 else allSectors,
        region__in=regions if len(regions) > 0 else regionsOriginal,
        title__icontains = searchQuery if searchQuery else ""
    ).distinct()[startIndex:endIndex]
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
        "regions": regions,
        "form": form,
        "url": url,
        "year": year
    }

    return render(request, 'pages/jobs.html', context)

def job_detail(request, slug):
    incrementView(request)
    year = datetime.now().year
    url = request.path_info
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sendEmailBack(form)
            messages.success(request, 'Thanks !! Your message is successfully submitted. We will contact you soon.')
            return HttpResponseRedirect(url)


    job = get_object_or_404(Job, slug=slug) 
    relatedJobs = Job.objects.filter(sectors__in = [sector.id for sector in job.sectors.all()]).distinct().exclude(slug = slug)[:4]

    context = {
        'slug': slug,
        "job": job,
        "relatedJobs": relatedJobs,
        "form":form,
        "url": url,
        "year": year
    }
    return render(request, 'pages/job-detail.html', context)

def companies(request:HttpRequest):
    incrementView(request)
    year = datetime.now().year
    url = request.path_info
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sendEmailBack(form)
            messages.success(request, 'Thanks !! Your message is successfully submitted. We will contact you soon.')
            return HttpResponseRedirect(url)
 
    page = 0
    if request.method == "GET" and request.GET.get("page"):
        page = int(request.GET.get("page"))


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
        "total": total,
        "form": form,
        "url": url,
        "year": year
    }
    return render(request, 'pages/companies.html', context)

def company_detail(request, slug):
    incrementView(request)
    year = datetime.now().year
    url = request.path_info
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sendEmailBack(form)
            messages.success(request, 'Thanks !! Your message is successfully submitted. We will contact you soon.')
            return HttpResponseRedirect(url)
    page = 0
    if request.method == "GET" and request.GET.get("page"):
        page = int(request.GET.get("page"))


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
        "total": total,
        "form": form,
        "url": url,
        "year": year
    }

    return render(request, 'pages/company-detail.html', context)