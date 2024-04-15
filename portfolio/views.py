from django.shortcuts import render,get_object_or_404
from .models import Project
# Create your views here.



def portfolio(request):
    projects=Project.objects.all()
    return render(request,'portfolio/portfolio.html',{'projects':projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    template_name = 'portfolio/wormyreads_detail.html'  # Template for Wormy Reads project
    template_name = 'portfolio/dialect.html'  # Template for Wormy Reads project

    return render(request, 'project_detail.html', {'project': project, 'template_name': template_name})
