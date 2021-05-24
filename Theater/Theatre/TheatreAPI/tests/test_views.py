from django.test import TestCase , Client
from django.urls import reverse
from TheatreAPI.models import Customer , Vacated_Seats
from django.conf import settings
from uuid import uuid4
class TestViews(TestCase):
	def setUp(self):
		self.client = Client()       # Every test needs a client.
		self.occupy_url = reverse('occupy') # occupy url 

	# if the name is not passed
	def test_occupy_if_name_not_passed_POST(self):   
		response = self.client.post(self.occupy_url)
		self.assertEquals(response.status_code,400)


	# if the name is passed
	def test_occupy_name_passed_POST(self):  
		response = self.client.post(self.occupy_url ,{"name":"Aryan Gupta"})
		self.assertEquals(response.status_code,200)


	# if seats are full
	def test_occupy_if_seats_are_full_Post(self):  
		for i in range(1,settings.MAX_OCCUPANCY+1):
			Customer.objects.create(name = f'Aryan{i}',seatno = i)
		response = self.client.post(self.occupy_url ,{"name":"Aryan Gupta"})
		self.assertEquals(response.status_code,204)
		self.assertEquals(response.data['Failure'],"Seats full")

	# if seats are full, then vacated one and again issued a ticket
	def test_occupy_if_seats_are_full_delete_then_again_occupy_Post(self):  
		for i in range(1,settings.MAX_OCCUPANCY+1):
			Customer.objects.create(name = f'Aryan{i}',seatno = i)
		response = self.client.post(self.occupy_url ,{"name":"Aryan Gupta"})
		self.assertEquals(response.status_code,204)
		self.assertEquals(response.data['Failure'],"Seats full")
		response = self.client.delete(reverse('vacate',args=[settings.MAX_OCCUPANCY-1]))
		self.assertEquals(response.status_code,200)
		response = self.client.post(self.occupy_url,{"name":"Aryan Gupta"})
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.data["Sucess"],f"Seat number is {settings.MAX_OCCUPANCY-1}")


	#Testing Vacate
	# if the seat is occupied
	def test_vacate_seat_occupied_delete(self):      
		Customer.objects.create(name = "Aryan Gupta",seatno = 1)
		response = self.client.delete(reverse('vacate',args=[1]))
		self.assertEquals(response.status_code,200)
		
	# if the seat is not occupied
	def test_vacate_seat_not_occupied_delete(self): 
		response = self.client.delete(reverse('vacate',args=[2]))
		self.assertEquals(response.status_code,204)



	# Testing get_info
	# if the seat is present
	def test_get_info_seat_GET(self):                    
		Customer.objects.create(name = "Aryan Gupta",seatno = 1)
		response = self.client.get(reverse('get_info',args=[1]))
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.data['Ticket']['name'],'Aryan Gupta')


	 # if the seat is not present
	def test_get_info_seat_not_present_GET(self): 
		Customer.objects.create(name = "Aryan Gupta",seatno = 1)
		response = self.client.get(reverse('get_info',args = [2]))
		self.assertEquals(response.status_code,400)

	# if the name is present
	def test_get_info_name_GET(self):                    
		Customer.objects.create(name = "Aryan Gupta",seatno = 1)
		response = self.client.get(reverse('get_info',args=["Aryan Gupta"]))
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.data['Ticket'][0]['seatno'],1)

	# if the name is not  present
	def test_get_info_name_not_present_GET(self):         
		Customer.objects.create(name = "Aryan Gupta",seatno = 1)
		response = self.client.get(reverse('get_info',args=['Shanker']))
		self.assertEquals(response.status_code,400)

	#if the ticket_id is present
	def test_get_info_ticket_id_present_GET(self):
		Customer.objects.create(name = "Aryan Gupta",seatno = 1)
		ticket_id = Customer.objects.get(seatno = 1).ticket_id
		response = self.client.get(reverse('get_info',args=[ticket_id]))
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.data['Ticket']['name'],'Aryan Gupta')

	#if the ticket_id is not present
	def test_get_info_ticket_id_not_present_GET(self):
		Customer.objects.create(name = "Aryan Gupta",seatno = 1)
		ticket_id = uuid4() 
		response = self.client.get(reverse('get_info',args=[ticket_id]))
		self.assertEquals(response.status_code,400)




