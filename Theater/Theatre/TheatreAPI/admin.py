from django.contrib import admin
from .models import Customer,Vacated_Seats
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','ticket_id',"seatno"]
@admin.register(Vacated_Seats)
class Vacated_SeatsAdmin(admin.ModelAdmin):
	list_display = ['vacated_seat']
