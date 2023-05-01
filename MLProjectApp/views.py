from django.shortcuts import render, HttpResponse
from datetime import datetime
from MLProjectApp.admin import Contact
from django.contrib import messages
import pandas as pd
import pickle
import numpy as np

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        error_message = None
        # Validation

        if(not name):
            error_message = "Name Required!!"
        elif(len(name)<4):
            error_message = "Name Must Have Atleast 4 Character!!"
        elif(len(phone)<10):
            error_message = "Phone Number Must Have Atleast 10 Digits!!"
        elif(not phone.isnumeric()):
            error_message = "Phone Number Must Be Numeric!!"

        # Saving
        if(not error_message):
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, 'Your message has been sent!')
        else:
            return render(request, 'contact.html', {'error': error_message})
    return render(request, 'contact.html')