from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterFormIntern, RegisterFormCompany
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def home_view(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterFormIntern(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = RegisterFormIntern()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def registerCompany(request):
    if request.method == 'POST':
        form = RegisterFormCompany(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = RegisterFormCompany()
    return render(request, 'registerCompany.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def contact_view(request):
    return render(request, 'contact.html')


@login_required
def intern_profile(request,username):
    return render(request, 'intern-profile.html')

@login_required
def company_profile(request):
    return render(request, 'company-profile.html')


def post_job(request):
    return render(request, 'post_job.html')


def listOfApplicants(request):
    return render(request, 'listOfApplicants.html')


def searchResults(request):
    return render(request, 'search-results.html')
