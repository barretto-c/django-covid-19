from django.shortcuts import render

# Create your views here.

from datetime import datetime

from info.forms import CovidDataForm
from info.models import CovidData

from django.views.generic import ListView,CreateView

from django import forms

#REST 
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.views import APIView
from . serializers import CovidDataSerializer

class HomeListViewNew(ListView):
    queryset = CovidData.objects.all()
    template_name = "info/home_new.html"

class CovidDataCreateForm(forms.ModelForm):
    class Meta:
        model= CovidData
        fields = '__all__'
        #fields = ['country_region', 'province_state', 'fips',  'active_cases' ]
        
class CovidDataCreateViewV2(CreateView):
    model = CovidData
    form_class = CovidDataCreateForm
    template_name = "info/covid_create.html"

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
            return redirect("home-new")
    else:
        return render(request, "info/enter_data.html", {"form": form})

class CovidDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CovidData.objects.all()
    serializer_class = CovidDataSerializer
