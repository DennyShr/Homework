from django.db import models

class InstanceDish(models.Model):
	name = models.CharField('Name', max_length=30)
	description = models.TextField('Description', max_length=255)
	is_vegan = models.BooleanField('Vegan')
	price = models.DecimalField('Price', max_digits=5, decimal_places=2)
	weight = models.IntegerField('Weight, grams')
	calories = models.IntegerField('Calories')

	def __str__ (self):
		return '{}'.format(self.name)

class DishCount(models.Model):
	dish = models.ForeignKey(InstanceDish, on_delete=models.CASCADE)
	order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
	count = models.IntegerField('Count', default=1)
