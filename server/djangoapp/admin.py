from django.contrib import admin
from .models import CarMake, CarModel


# Inline model for CarModel inside CarMake
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


# Admin for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'dealer_id')


# Admin for CarMake with inline CarModels
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]


# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)