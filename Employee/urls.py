from django.urls import path
from Employee import views

app_name = 'Employee'

urlpatterns = [

    # Employee App Urls
    path("employee/profile/details/", views.EmployeeRegistrationAPIview.as_view()),
    
]