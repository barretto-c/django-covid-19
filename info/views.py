from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import re
from datetime import datetime

from django.shortcuts import redirect
from info.forms import CovidDataForm
from info.models import CovidData

from django.views.generic import ListView

from django.contrib import admin

admin.site.register(CovidData)

def home(request):
    #return HttpResponse("Hello, Django!")
    return render(request, "info/home.html")

class HomeListView(ListView):
    """Renders the home page, with data."""
    model = CovidData

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

    
def about(request):
    return render(request, "info/about.html")

def contact(request):
    return render(request, "info/contact.html")

# Add this code elsewhere in the file:
def logdata(request):
    form = CovidDataForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("home")
    else:
        return render(request, "info/enter_data.html", {"form": form})


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