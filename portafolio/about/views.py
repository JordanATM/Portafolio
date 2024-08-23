from django.shortcuts import render
from .models import Course, Skill

# Create your views here.

def about(request):
    Courses = Course.objects.all()
    Skills = Skill.objects.all()
    return render(request, 'about/about.html', {'Courses': Courses, 'Skills': Skills})