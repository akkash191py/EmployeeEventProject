from rest_framework import serializers
from Employee.models import Employee, EventDetails

class EmployeeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeRegisterSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["first_name","last_name","email","phoneNumber","gender","DOB","joining_date"]

class EventSerialzer(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = '__all__'