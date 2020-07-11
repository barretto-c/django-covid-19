from rest_framework import serializers

from info.models import CovidData

# class CovidDataSerializer(serializers.HyperlinkedModelSerializer):
class CovidDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidData
        fields = '__all__'
