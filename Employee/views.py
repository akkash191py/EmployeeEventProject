from django.shortcuts import render
from rest_framework.views import APIView
import smtplib
from django.conf import settings
from email.message import EmailMessage
from django.core.mail import send_mail
from email.utils import formataddr
from rest_framework.response import Response
from Employee.models import Employee, EventDetails
from Employee.serializers import EmployeeSerialzer, EmployeeRegisterSerialzer, EventSerialzer
import datetime
from Employee.tasks import send_birthday_anniversary_wishes


# Create your views here.
class EmployeeRegistrationAPIview(APIView):
    
    def get(self, request):
        empObj=Employee.objects.all()
        jsonData = EmployeeSerialzer(empObj, many=True)
        empProfile = jsonData.data
        return Response({"status": "success","message":"Basic Profile fetched successfully","data":empProfile},status=200)
    
    def post(self, request, *args, **kwargs):

        email = request.data.get('email', False)
        mobile = request.data.get('phoneNumber', False)
        first_name = request.data.get('first_name', False)
        last_name = request.data.get('last_name', False)
        dob = request.data.get('DOB', False)
        joining_date = request.data.get('joining_date', False)
        gender = request.data.get('gender', False)

        
        
        try:  
            user = Employee(email=email, first_name = first_name, last_name = last_name,
                                phoneNumber = mobile, DOB= dob, joining_date = joining_date, 
                                gender=gender)
            
            user.save()
            empRegSerialzer = EmployeeRegisterSerialzer(user, many=False).data
            return Response({"status":"success","message":"Register success!", "data":empRegSerialzer},status=200)
        except:
            return Response({"status": "warning","message":"Invalid inputes!","errors":empRegSerialzer.errors},status=400)

       
class EmployeeEventWishesAPIview(APIView):

    def get(self, request):
        eventObj=EventDetails.objects.all()
        jsonData = EventSerialzer(eventObj, many=True)
        eventData = jsonData.data
        return Response({"status": "success",
                         "message":"Event fetched successfully",
                         "data":eventData},status=200)
    

    def post(self, request, *args, **kwargs):

        # today = datetime.now().strftime("%d-%m")
        today = datetime.date.today()
        # year_now = datetime.now().strftime("%Y")

        upcoming_birthdays = Employee.objects.filter(
            DOB__month=today.month,
            DOB__day=today.day
        )
        upcoming_anniversary = Employee.objects.filter(
            joining_date__month=today.month,
            joining_date__day=today.day
        )

        
        for user_profile in upcoming_birthdays:
            birthDayWishes = "Dear" + user_profile.first_name, + ", Wishing you a great birthday and a memorable year, From all of us."
            event = EventDetails(empId=user_profile.id, event_type = "Birthday", wishes = birthDayWishes, eventDate = datetime.date)
            event.save()
            send_birthday_anniversary_wishes()
            self.stdout.write(self.style.SUCCESS(f"Sent birthday email to {user_profile.email}"))

        
        for user_event in upcoming_anniversary:
            birthDayWishes = "Dear" + user_event.first_name + ", Congratulations on your work anniversary! It’s a special day to celebrate your great work and dedication to your job over the years."
            eventAnniversay = EventDetails(empId=user_event.id, event_type = "Work Anniversary", wishes = birthDayWishes, eventDate = datetime.date)
            eventAnniversay.save()
            send_birthday_anniversary_wishes()
            self.stdout.write(self.style.SUCCESS(f"Sent birthday email to {user_event.email}"))

        return Response({"status":"success","message":"Event created successfully!!"},status=200)


