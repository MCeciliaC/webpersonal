from django.shortcuts import render, HttpResponse
from .models import Project, Study, Service, Credit

# Create your views here.
def home(request):
    return render(request, "portfolio/home.html")

def contact(request):
    services= Service.objects.all()
    return render(request, "portfolio/contact.html", {'services':services})

def portfolio(request):
    projects= Project.objects.all() 
    credit= Credit.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects,'credit':credit})

def about(request):
    education= Study.objects.all() 
    return render(request, "portfolio/about.html", {'education':education})
