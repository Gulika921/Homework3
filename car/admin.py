from django.contrib import admin
from .models import Car, CarModel, Company, CarColour, CarReleaseDate, CarType
# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "vin_number",
        "car_model",
        "company",
    ]
    fieldsets = (
        (None, {
            'fields': (
                ("name", "vin_number"),
            )
        }),
        ('Advanced options', {
            'fields': (("car_model", "company"), ("car_colour", "car_release_date"), "car_type")
        }),
    )
    readonly_fields = [
        "company"
    ]


class CarInline(admin.StackedInline):
    model = Car

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
    inlines = [
        CarInline,
    ]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(CarColour)
class CacrColourAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(CarReleaseDate)
class CarReleaseDateAdmin(admin.ModelAdmin):
    list_display = [
        "date"
    ]


@admin.register(CarType)
class CarReleaseDateAdmin(admin.ModelAdmin):
    list_display = [
        "type"
    ]
