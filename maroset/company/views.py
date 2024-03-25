from django.shortcuts import render

# Create your views here.
def company_regsiter(request):
    return render(request, 'company/home.html')