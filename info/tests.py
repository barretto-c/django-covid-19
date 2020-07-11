from django.test import TestCase
from info.models import CovidData

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
