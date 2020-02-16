#from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Location

from .serializers import LocationSerializer
from .pagination import CustomPagination
import json
# Create your views here.


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
	
#def location(request):
#	data = {}
#	data['city1'] = 'London'
#	jdata  = json.dumps(data)
#	return HttpResponse(jdata)
	
class get_locations(ListCreateAPIView):
    serializer_class = LocationSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self,lat,long):
       query = "select id, name, state_id, state_code, country_id, country_code, latitude, longitude, (6371 * acos( cos( radians(latitude) ) * cos(radians("+lat+") ) * cos(radians("+long+") - radians(longitude) ) + sin( radians(latitude) ) * sin( radians("+lat+") ) ) ) as distance from location_location order by distance LIMIT 10"
       print(query)
       locations =  Location.objects.raw(query)
       return locations

    # Get all movies
    def get(self, request):
        body = json.loads(request.body)
        lat = body['latitude']
        long = body['longitude']
        print(lat,long)
        locations = self.get_queryset(lat,long)
        paginate_queryset = self.paginate_queryset(locations)
        print(paginate_queryset)
        serializer = self.serializer_class(paginate_queryset, many=True)
        print("h5")
        temp = self.get_paginated_response(serializer.data)
        print("h6")
        return temp
