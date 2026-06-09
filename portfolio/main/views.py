from django.shortcuts import render
from .models import Project, Profile, Experience, Skill


def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experience = Experience.objects.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experience': experience,
    }

    return render(request, 'main/index.html', context)