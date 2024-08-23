from django.shortcuts import render
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'core/contact.html', {'contacts': contacts})

