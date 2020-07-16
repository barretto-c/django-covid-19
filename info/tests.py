from django.test import TestCase
from info.models import CovidData

from django.urls import reverse
import json

# Create your tests here.
class CovidTestCase(TestCase):
    def setUp(self):
        CovidData.objects.create(
            fips=45001,
            country_region="US",
            province_state="South Carolina",
            active_cases=124,
        )
        CovidData.objects.create(
            fips=22001,
            country_region="US",
            province_state="Louisiana",
            active_cases=976,
        )

    def test_check_setup_data_count(self):
        count = CovidData.objects.count()
        self.assertEqual(count, 2)

    def test_check_valid_data(self):
        fips_45001 = CovidData.objects.filter(fips=45001).values()
        self.assertEqual(fips_45001[0]["country_region"], "US")
        self.assertEqual(fips_45001[0]["active_cases"], 124)

    def test_data_add(self):
        CovidData.objects.create(
            fips=12095,
            country_region="US",
            province_state="Florida",
            active_cases=50000,
        )
        count = CovidData.objects.count()
        self.assertEqual(count, 3)

    def test_view_homepage(self):
        response = self.client.get(reverse('home-new'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home page for the COVID-19")

    def test_logdata_create_page(self):
        response = self.client.get(reverse('logdata'))
        self.assertEqual(response.status_code, 200)