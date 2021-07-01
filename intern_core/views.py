from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def contact_view(request):
    return render(request, 'contact.html')


def intern_profile(request):
    return render(request, 'intern-profile.html')


def company_profile(request):
    return render(request, 'company-profile.html')


def post_job(request):
    return render(request, 'post_job.html')


def listOfApplicants(request):
    return render(request, 'listOfApplicants.html')


