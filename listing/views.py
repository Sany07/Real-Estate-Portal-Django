from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request,'site/index.html')


def About(request):
    return render(request,'site/about.html')


def Listings(request):
    return render(request,'site/listings.html')