from django.shortcuts import render

# Create your views here.
def candidate_home(request):
    return render(request, 'candidate/home.html')