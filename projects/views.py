from django.shortcuts import render
from projects.models import Projects


def project_index(request):
    projects = Projects.objects.all().order_by('id')
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)
