from django.db import models

# Create your models here.

class CovidData(models.Model):
    id = models.AutoField(primary_key=True)
    fips = models.IntegerField()
    country_region = models.CharField(max_length=50)
    province_state = models.CharField(max_length=50)
    active_cases = models.IntegerField(blank=True, null=True)

    def __str__(self):
        """Returns a string representation of Entry."""
        return f"'Active Cases in {self.country_region}, {self.province_state} = {self.active_cases}"