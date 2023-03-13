from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/<slug:slug>/', views.job_detail),
    path('companies/', views.companies, name='companies'),
    path('companies/<slug:slug>/', views.company_detail, name='company_detail'),


]