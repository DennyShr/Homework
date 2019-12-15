from django import forms
from django.forms import ModelForm
from .models import Order

class OrderCreate(ModelForm):
	class Meta:
		model = Order
		fields = ['costumer_name', 'dish_ordered']

	def get_order(self):
		return self.cleaned_data.get('order')
		
class DishesAddForm(forms.Form):
	count = forms.IntegerField(label='How many?')

	def get_count(self):
		return self.cleaned_data.get('count')

