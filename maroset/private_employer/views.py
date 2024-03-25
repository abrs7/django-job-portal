from django.shortcuts import render

# Create your views here.


def private_employer(request):
    return render(request, 'private/home.html')
