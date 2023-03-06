from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/home.html', { "isHomeActive": True })

def jobs(request):
    return render(request, 'pages/jobs.html', { "isJobsActive": True })

def job_detail(request, slug):
    return render(request, 'pages/job-detail.html', { 'slug': slug})

def companies(request):
    return render(request, 'pages/companies.html', { "isCompaniesActive":True})

def company_detail(request, slug ):
    return render(request, 'pages/company-detail.html', context={ 'slug':slug })