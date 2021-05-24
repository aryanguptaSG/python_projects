from rest_framework import serializers
from .models import Customer,Vacated_Seats


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('seatno','name','ticket_id')
class Vacated_SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacated_Seats
        fields = ('vacated_seat',)