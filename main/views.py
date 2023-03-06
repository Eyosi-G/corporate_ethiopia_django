from django.shortcuts import render
from .models import Company
from django.http import HttpRequest
# Create your views here.

def home(request):
    return render(request, 'pages/home.html', { "isHomeActive": True })

def jobs(request):

    return render(request, 'pages/jobs.html', { "isJobsActive": True })

def job_detail(request, slug):
    return render(request, 'pages/job-detail.html', { 'slug': slug})

def companies(request:HttpRequest, page = 0):
    startIndex = page * 10
    endIndex = startIndex + 10
    total = Company.objects.count()
    companies = Company.objects.all()[startIndex:endIndex]
    numOfPages = int(total / 10)
    context = {
        "companies": companies,
        "isCompaniesActive":True,
        "currentPage": page + 1,
        "numOfPages": numOfPages + 1
    }
    return render(request, 'pages/companies.html', context)

def company_detail(request, slug ):
    return render(request, 'pages/company-detail.html', context={ 'slug':slug })