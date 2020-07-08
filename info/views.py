from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import re
from datetime import datetime


def home(request):
    #return HttpResponse("Hello, Django!")
    return render(request, "info/home.html")

def about(request):
    return render(request, "info/about.html")

def contact(request):
    return render(request, "info/contact.html")

def dashboard(request, region):
    return render(
        request,
        'info/dashboard.html',
        {
            'region': region,
            'date': datetime.now()
        }
    )

# def dashboard(request, region):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     content = "It's " + formatted_now
#     return HttpResponse(content)