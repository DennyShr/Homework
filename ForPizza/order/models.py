from django.db import models

class Order(models.Model):
	costumer_name = models.CharField('Name', max_length=100, default='Unknown')
	dish_ordered = models.ManyToManyField('dishes.InstanceDish', through='dishes.DishCount')

	def __str__ (self):
		return '{}'.format(self.id)

	def get_absolute_url(self):
		return reverse('order-detail', kwargs={'pk': self.pk})
