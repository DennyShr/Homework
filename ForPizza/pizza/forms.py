from django import forms
from .models import PizzaName

class PizzaAddForm(forms.Form):
	name = forms.CharField(label='Pizza', max_length=30)
	price = forms.DecimalField(label='Price', max_digits=5, decimal_places=2)
	weight = forms.IntegerField(label='Weight, grams')

	def create_objects(self):
		PizzaName.objects.create(
			name = self.cleaned_data.get('name'),
			price = self.cleaned_data.get('price'),
			weight = self.cleaned_data.get('weight')
			)

