from django.shortcuts import render
from .models import Project
# Create your views here.

def portfolio(request):
    projects=Project.object.all()
    return render(request,'portfolio/portfolio.html',{'projects':projects})