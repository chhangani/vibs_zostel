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

# Class for handling API request
class get_locations(ListCreateAPIView):
	# We need to serialize data from query result set to join data
    serializer_class = LocationSerializer
	# pagination 10 results will be displayed.
    pagination_class = CustomPagination
    
	# Method function for fetching results, We used Haversine formula to calculate results
    def get_queryset(self,lat,long):
       query = "select id, name, state_id, state_code, country_id, country_code, latitude, longitude, (6371 * acos( cos( radians(latitude) ) * cos(radians("+lat+") ) * cos(radians("+long+") - radians(longitude) ) + sin( radians(latitude) ) * sin( radians("+lat+") ) ) ) as distance from location_location order by distance LIMIT 10"
       locations =  Location.objects.raw(query)
       return locations

    # Get all cities requests
    def get(self, request):
        body = json.loads(request.body) # Data will be in request body only.
        lat = body['latitude']  # Fetching latitude value
        long = body['longitude'] # Fetching longitude value
        locations = self.get_queryset(lat,long) # We are calling one of member function of class.
        paginate_queryset = self.paginate_queryset(locations) # Pagination (Not needed)
        serializer = self.serializer_class(paginate_queryset, many=True) # Response conversion
        temp = self.get_paginated_response(serializer.data)
		# Just storing the data in a temp, not now but in future we may need to apply some validation on this, so i am storing it separately.  
        return temp
