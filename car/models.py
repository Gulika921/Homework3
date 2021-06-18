from django.db import models

# Create your models here.
TR = 'Tr'
OR = 'Or'
PC = 'Pc'
CAR_TYPES = [
    (TR, 'Truck'),
    (OR, 'Off-roader'),
    (PC, 'Passenger car'),
]


class Car(models.Model):
    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    car_model = models.ForeignKey("car.CarModel", on_delete=models.SET_NULL, null=True)
    car_colour = models.ForeignKey("car.CarColour", blank=True, null=True, on_delete=models.SET_NULL)
    car_release_date = models.ForeignKey("car.CarReleaseDate", blank=True, null=True, on_delete=models.SET_NULL)
    car_type = models.ForeignKey("car.CarType", blank=True, null=True, on_delete=models.SET_NULL, choices=CAR_TYPES)

    def company(self):
        return self.car_model.company

    def __str__(self):
        return f"Name:{self.name} vin_number: {self.vin_number}"


class CarModel(models.Model):

    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class CarColour(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarReleaseDate(models.Model):

    date = models.CharField(max_length=100)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name_plural = "Cars release dates"


class CarType(models.Model):

    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
