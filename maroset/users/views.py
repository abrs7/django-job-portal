from django.shortcuts import redirect, render
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
from .models import User
from .forms import RegistrationUserForm
from resume.models import Resume
from company.models import Company
from private_employer.models import PrivateRecruiter

def register_candidate(request):
    if (request.method == 'POST'):
        form = RegistrationUserForm(request.POST)
        if form.is_valid:
            var = form.save(commit=False)
            var.is_candidate = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been created!')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong!')
            return redirect('register-candidate')
    else:
        form = RegistrationUserForm()
        context = {'form': form }
        return render(request, 'users/register_candidate.html', context)
    

# Register Recruiter Only
def register_company(request):
    if (request.method == 'POST'):
        form = RegistrationUserForm(request.POST)
        if form.is_valid:
            var = form.save(commit=False)
            var.is_company = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created!')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong!')
            return redirect('register-company')
    else:
        form = RegistrationUserForm()
        context = {'form': form }
        return render(request, 'users/register_company.html', context)

def register_private_recruiter(request):
    if (request.method == 'POST'):
        form = RegistrationUserForm(request.POST)
        if form.is_valid:
            var = form.save(commit=False)
            var.is_private_employer = True
            var.username = var.email
            var.save()
            PrivateRecruiter.objects.create(user=var)
            messages.info(request, 'Your account has been created!')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong!')
            return redirect('register-private-recruiter')
    else:
        form = RegistrationUserForm()
        context = {'form': form }
        return render(request, 'users/register_private_recruiter.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username= email, password = password)
        if user is not None and user.is_active:
            login(request, user)
            if request.user.is_candidate:
                return redirect('candidate-dashboard')
            elif request.user.is_company:
                return redirect('company-dashboard')
            elif request.user.is_private_employer:
                return redirect('private-employer-dashboard')
            else:
                return redirect('login')
        else:
            messages.warning(request,'Something went wrong. Please check your credentials.')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended.')
    return redirect('login')



   