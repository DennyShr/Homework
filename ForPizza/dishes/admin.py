from django.contrib import admin
from .models import  InstanceDish, DishCount

class InstanceDisName(admin.ModelAdmin):
	list_display = ('name', 'is_vegan', 'price')

admin.site.register(InstanceDish, InstanceDisName)
admin.site.register(DishCount)