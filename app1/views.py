from typing import Container
from django.shortcuts import render,HttpResponse
from datetime import datetime
from app1.models import Contact


# Create your views here.
def index(request):
    context={
        'variable':' is equal to = sagar khare',
        'variable2': 'is equal to = anjali khare'
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is my new application")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is the best hotel in nashik by sagar khare")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("Our services is best in nashik.")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email,phone=phone,desc=desc,date
        =datetime.today)
        contact.save()

    return render(request,'contact.html')
    #return HttpResponse("This is my contact number -12345")
