from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def jobs(request):
    return render(request, 'pages/jobs.html')

def companies(request):
    return render(request, 'pages/companies.html')

def company_detail(request, slug ):
    return render(request, 'pages/company-detail.html', context={ 'slug':slug })