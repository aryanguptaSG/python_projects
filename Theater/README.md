
**First of all install all the requirements.**
**There are three end points in the given app.**

	1. /occupy/
	 	It is used to generate the ticket for the user.
	 	It accepts the name of the person in json format as specified below:
	 				{
	 					"name":NameOfThePerson
	 				}

	2. /vacate/seat_number
		It is used to free the given seat.In place of seatnumber who have to give the seatnumber.
		For example : If you want to free the seat_number 6, then you should request as
		http://localhost:8000/vacate/6

	3.  /get_info/<Name or seat_number or ticket_id>
	    It is used to fetch the ticket details. It takes either name or seat_number or ticket_id.
	    3.a For example : If you want to get the info for  the **seat_number** 6, then you should request as
					http://localhost:8000/get_info/6
			3.b In case of name :
					It returns list of all the tickets with the given name.


You can change the number of seats by changing the value of **MAX_OCCUPANCY** variable in the django settings.py file.
To **test the django app** ,you may fire the command : "python manage.py test TheatreAPI"
