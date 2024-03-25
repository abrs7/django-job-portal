from django.shortcuts import render, redirect

# Create your views here.

def proxy(request):
    if request.user.is_candidate :
        return redirect('candidate-dashboard')
    elif request.user.is_company:
        return redirect('company-dashboard')
    elif request.user.is_private_employer:
        return redirect('private-recruiter-dashboard')
    else:
        return('login')
    


def candidate_dashboard(request):
    return render(request,'dashboard/candidate_dashboard.html')

def company_dashboard(request):
    return render(request,'dashboard/company_dashboard.html')

def private_recruiter_dashboard(request):
    return render(request,'dashboard/private_recruiter_dashboard.html')

