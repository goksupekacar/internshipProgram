from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact_view, name='contact'),
    path('postJob', views.post_job, name='postJob'),
    path('intern-profile/', views.intern_profile, name='internProfile'),
    path('company-profile/', views.company_profile, name='company-profile'),
    path('listOfApplicants/', views.listOfApplicants, name='listOfApplicants'),
]
