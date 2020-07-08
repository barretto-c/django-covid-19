from django import forms
from info.models import CovidData

class CovidDataForm(forms.ModelForm):
    class Meta:
        model = CovidData
        fields = ("id", "fips", "country_region", "province_state", "active_cases", )
