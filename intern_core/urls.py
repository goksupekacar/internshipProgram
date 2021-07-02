from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register, name='register'),
    path('register-company/', views.registerCompany, name='register-company'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('postJob', views.post_job, name='postJob'),
    path('intern-profile/<str:username>', views.intern_profile, name='internProfile'),
    path('company-profile/', views.company_profile, name='company-profile'),
    path('listOfApplicants/', views.listOfApplicants, name='listOfApplicants'),
    path('search-results/', views.searchResults, name='searchResults'),

]
