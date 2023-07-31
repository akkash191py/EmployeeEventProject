from django.contrib import admin
from Employee.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
     list_display=["id","first_name","last_name","email", "phoneNumber", "DOB", "joining_date"]

admin.site.register(Employee, EmployeeAdmin)