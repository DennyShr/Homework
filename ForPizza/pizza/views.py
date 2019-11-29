from django.views.generic import ListView, TemplateView
from django.views import View
from .models import PizzaName, PizzaOrdered
from django.http import HttpResponse
from .forms import PizzaAddForm
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy

class PizzasList(ListView):
	model = PizzaName
	template_name = 'pizza/pizza.html' #template_name = '(modelname)_list.html' - by default

class PizzaTemplateView(TemplateView):
	template_name = 'pizza/pizza_template.html'

class MyView(View):
	def get(self, request):
		return HttpResponse("Hello, it's view")

class PizzaAddView(FormView):
	template_name = 'pizza/pizzaadd.html'
	form_class = PizzaAddForm
	success_url = '.'

	def form_valid(self, form):
		form.create_objects()
		return super().form_valid(form)


