from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('companies/', views.companies, name='companies'),
    path('companies/<slug:slug>/', views.company_detail)

]