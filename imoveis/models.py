from django.db import models
from django.utils import timezone

class Country(models.Model):
	country 		= models.CharField(max_length=80)
	currency 		= models.CharField(max_length=40)
	currency_symbol = models.CharField(max_length=10)

class Real_State(models.Model):
	real_state 	= models.CharField(max_length=80)
	site		= models.URLField()

class Property_Type(models.Model):
    property_type = models.CharField(max_length=40)

class Neighborhood(models.Model):
	neighborhood = models.CharField(max_length=80)			

class Property(models.Model):
    real_state_id 		= models.ForeignKey('Real_State')
    property_id			= models.CharField(max_length=40)
    property_name		= models.CharField(max_length=80)
    property_type_id 	= models.ForeignKey('Property_Type')
    beds 				= models.IntegerField()
    baths				= models.IntegerField()
    days				= models.IntegerField()
    home_size			= models.DecimalField(max_digits=8, decimal_places=2)
    lot_size			= models.DecimalField(max_digits=8, decimal_places=2)
    home_age			= models.IntegerField()
    garage				= models.IntegerField()
    neighborhood		= models.ForeignKey('Neighborhood')
    price				= models.DecimalField(max_digits=14, decimal_places=2)
    items				= models.TextField()
    created_date 		= models.DateTimeField(default=timezone.now)

    def search(self):
    	self.save()

    def __str__(self):
        return self.property_id
        
