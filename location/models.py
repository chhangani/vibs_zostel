from django.db import models

 # Create Location Model
class Location(models.Model):
    name = models.CharField(max_length=255)
    state_id = models.IntegerField()
    country_id = models.IntegerField()
    country_code = models.CharField(max_length=4)
    latitude = models.DecimalField(..., max_digits=10, decimal_places=8)
    longitude = models.DecimalField(..., max_digits=11, decimal_places=8)
    flag = models.IntegerField()
    wikiDataId = models.CharField(max_length=255)




