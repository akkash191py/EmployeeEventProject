from django.contrib import admin
from Employee.models import Employee, EventDetails


# Register EmployeeAdmin models here.
class EmployeeAdmin(admin.ModelAdmin):
     list_display=["id","first_name","last_name","email", "phoneNumber", "DOB", "joining_date"]

admin.site.register(Employee, EmployeeAdmin)


class EventDetailsAdmin(admin.ModelAdmin):
     list_display=["id", "empId", "event_type", "eventDate"]

admin.site.register(EventDetails, EventDetailsAdmin)
