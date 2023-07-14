from django.shortcuts import render,redirect
from .models import Name
# Create your views here.
def index(request):
    
    return render(request,'index.html')


    

def display(request):
    
    n=Name.objects.all()
    return render(request,"display.html",{'info':n})