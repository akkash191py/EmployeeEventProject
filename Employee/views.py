from django.shortcuts import render
from rest_framework.views import APIView
import smtplib
from django.conf import settings
from email.message import EmailMessage
from django.core.mail import send_mail
from email.utils import formataddr
from rest_framework.response import Response
from Employee.models import Employee
from Employee.serializers import EmployeeSerialzer, EmployeeRegisterSerialzer
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

    def post(self, request):
        pass


