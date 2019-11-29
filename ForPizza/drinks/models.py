from django.db import models

class Drink(models.Model):
	name = models.CharField('Drink', max_length=50)
	volume = models.IntegerField('Volume, ml', default=0)
	price = models.DecimalField('Price, hrn', max_digits=5, decimal_places=2, default=0)