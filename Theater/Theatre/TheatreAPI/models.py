# Create your models here.
from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
class Customer(models.Model):
	name = models.CharField(max_length=50,null=False)
	ticket_id =  models.UUIDField( default = uuid4, editable = False)
	seatno = models.PositiveIntegerField(primary_key = True ,validators=[MinValueValidator(1), MaxValueValidator(settings.MAX_OCCUPANCY)])
class Vacated_Seats(models.Model):
	vacated_seat = models.PositiveIntegerField()

	
