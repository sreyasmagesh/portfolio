from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def download(request):
    return render(request,'download.html')


def contact(request):
    return render(request,'contact.html')


def artwork(request):
    return render(request,'artwork.html')
