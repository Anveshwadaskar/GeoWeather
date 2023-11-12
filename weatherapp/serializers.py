from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class meta:
        model = Location
        fields = '__all__'