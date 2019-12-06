from django import forms
from django.forms import ModelForm
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

class PizzaAddModelForm(ModelForm):
	class Meta:
		model = PizzaName
		fields = ['name', 'price', 'weight']