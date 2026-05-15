# Ex01 Django ORM Web Application
## Date: 15.05.2025

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
models.py

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

admin.py
    
from django.contrib import admin
from .models import (Food_ordering,Food_orderingAdmin)
admin.site.register(Food_ordering,Food_orderingAdmin)    
```

## OUTPUT

![alt text](<Screenshot 2025-09-16 154131.png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
