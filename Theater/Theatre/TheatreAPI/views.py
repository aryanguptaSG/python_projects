from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CustomerSerializer,Vacated_SeatsSerializer
from .models import Customer,Vacated_Seats

@api_view(['POST'])
def occupy(request):
	name = request.data.get("name",None)
	if name:
		seatno = 0
		if not Vacated_Seats.objects.first():
			if Customer.objects.first(): 
				seatno = Customer.objects.last().seatno
			data = {"name" :name,"seatno":seatno+1}
		else:
			old_seat = Vacated_Seats.objects.first()
			data = {"seatno":old_seat.vacated_seat,"name" :name}
			old_seat.delete()
		ticket_gen = CustomerSerializer(data = data)
		if ticket_gen.is_valid():
			ticket_gen.save()
			return Response({'Sucess':f"Seat number is {ticket_gen.data['seatno']}"},200)
		return Response({"Failure":"Seats full"},204)
	return Response({"Failure":"Name not passed"},400)


@api_view(['DELETE'])
def vacate(request,seat):
	try :
		if int(seat) and seat>0:
			ticket_over = Customer.objects.filter(seatno = seat).first()
			if ticket_over:
				old_id = ticket_over.seatno
				ticket_over.delete()
				data = {"vacated_seat":old_id}
				old_seat = Vacated_SeatsSerializer(data= data)
				if old_seat.is_valid():
					old_seat.save()
				return Response({"Sucess":f"{seat} vacated sucessfully"},200)
			else :
				return Response({"Failure":f"{seat} is already vacant"},204)
		else:
			return Response({"Failure":f"{seat} isn't a valid seat number"},400)

	except:
		return Response({"Failure":f"{seat} isn't a valid seat number"},400)


@api_view(['GET'])
def get_info(request,info):
	try :
		ticket = Customer.objects.get(ticket_id = info)
		ticket = CustomerSerializer(ticket)
		return Response({"Ticket":ticket.data},200)
	except:
		try:
			ticket = Customer.objects.get(seatno = int(info))
			ticket = CustomerSerializer(ticket)
			return Response({"Ticket":ticket.data},200)
		except:
			try:
				ticket = Customer.objects.filter(name = info)
				ticket = CustomerSerializer(ticket,many = True)
				if len(ticket.data)<1:
					return Response({"Error":"Details not found"},400)
				return Response({"Ticket":ticket.data},200)
			except:
				return Response({"Error":"Details not found"},400)




