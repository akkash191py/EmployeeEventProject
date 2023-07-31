from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

# Create Employee models here.
class Employee(models.Model):
    first_name = models.CharField('First Name', max_length=50, blank = False, null = False)
    last_name = models.CharField('Last Name', max_length=50, blank = False, null = False)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    phoneNumber = PhoneNumberField('Mobile number', max_length=15, 
                                   blank=False, null=False, unique=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=False, blank=False)
    DOB = models.DateField()
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Employees'
        verbose_name_plural = "Employee"

    def __str__(self):
        return str(self.first_name + "" + self.last_name)