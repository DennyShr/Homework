from django.contrib import admin
from .models import  Drink

class AdminDrink(admin.ModelAdmin):
	list_display = ('name', 'volume', 'price')

admin.site.register(Drink, AdminDrink)

