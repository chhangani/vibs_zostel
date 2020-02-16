from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Location
        fields = ('id', 'name', 'state_id', 'country_id', 'country_code', 'latitude', 'longitude', 'flag', 'wikiDataId')
