from django.contrib import admin
from .models import  PizzaName, Ingredient, Pizza, Every, PizzaOrdered

class AdminPizzaName(admin.ModelAdmin):
	list_display = ('name', 'price', 'weight')

class AdminIngredients(admin.ModelAdmin):
	list_display = ('name', 'price', 'weight', 'is_vegan')

admin.site.register(PizzaName, AdminPizzaName)
admin.site.register(Ingredient, AdminIngredients)
admin.site.register(Pizza)
admin.site.register(Every)
admin.site.register(PizzaOrdered)