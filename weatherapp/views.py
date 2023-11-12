from django.shortcuts import render
from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer
from django.contrib.gis.geos import Point
from django.conf import settings
import requests



class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        latitude = self.request.data.get('latitude')
        longitude = self.request.data.get('longitude')
        point = Point(float(longitude), float(latitude))

        weather_data = self.get_weather_data(latitude, longitude)

        serializer.save(point=point, temperature=weather_data.get('temperature', None),
                        humidity=weather_data.get('humidity', None))
        

    
    def get_weather_data(self, latitude, longitude):
        url = f'https://api.weather.gov/points/{latitude},{longitude}/forecast'
        headers = {'User-Agent': 'YourAppName/1.0 (your@email.com)'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            today_forecast = data['properties']['periods'][0]
            return {'temperature': today_forecast['temperature'], 'humidity': today_forecast['humidity']}
        else:
            return {'temperature': None, 'humidity': None}

        
   









