from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from .forms import OrderCreate, DishesAddForm
from dishes.models import InstanceDish, DishCount
from .models import Order
from django.views.generic import ListView, TemplateView
from django.db.models import Sum

class OrderCreateView(FormView):
	template_name = 'order/formtemplate.html'
	form_class = OrderCreate

	def form_valid(self, form):
		saving = form.save()
		self.success_url = '/order/add/order{}/'.format(saving.pk)
		return super().form_valid(form)

class DishesCountView(ListView):
	model = DishCount
	template_name = 'order/orderlisttemplate.html' #template_name = '(modelname)_list.html' - by default

	def get_queryset(self):
		queryset = DishCount.objects.filter(order=self.kwargs.get('pk'))
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['order'] = self.kwargs.get('pk')
		context['full_price'] = DishCount.objects.filter(order=self.kwargs.get('pk')).aggregate(Sum('dish__price'))
		return context

class ChangeCountForm(FormView):
	template_name = 'order/formtemplate.html'
	form_class = DishesAddForm

	def form_valid(self, form):
		DishCount.objects.filter(order=self.kwargs.get('pk'), dish=self.kwargs.get('name')).update(count=form.get_count())
		self.success_url = '/order/add/order{}/'.format(self.kwargs.get('pk'))
		return super().form_valid(form)

class ChangeOrder(UpdateView):
	model = Order
	fields = ['costumer_name', 'dish_ordered']
	template_name = 'order/formtemplate.html'

	def form_valid(self, form):
		self.success_url = '/order/add/order{}/'.format(self.kwargs.get('pk'))
		return super().form_valid(form)