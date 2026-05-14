from django.db import models
from django.contrib import admin
class Food_ordering(models.Model ):
    hotel_name=models.CharField(max_length=18)
    no_of_quantity=models.IntegerField(primary_key="card_ID")
    food_name=models.CharField(max_length=18)
    Food_rating=models.FloatField()
    Description=models.CharField(max_length=18)
class Food_orderingAdmin(admin.ModelAdmin):
    list_display=["hotel_name","no_of_quantity","food_name","Food_rating","Description"]
    