from django.views.generic import ListView
from .models import Drink

class DrinksList(ListView):
	model = Drink

# Create your views here.
