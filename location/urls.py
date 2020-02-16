from django.urls import path,include

from . import views

urlpatterns = [
#    path('', views.index, name='index'),
    path('api/v1/cities', views.get_locations.as_view(), name='get_locations'),
]