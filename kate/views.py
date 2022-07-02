from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    profile = Profile.objects.all()
    about = About.objects.all()
    skills = Skills.objects.all()
    project = Project.objects.all()
    contact = Contact.objects.all()
    return render(request,'index.html',{"profile":profile,"about":about,"skills":skills,"project":project,"contact":contact})