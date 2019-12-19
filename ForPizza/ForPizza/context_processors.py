from pizza.models import PizzaDiscount
from order.models import Order

def pizza_discount(request):
	return {"pizza_discount_list": PizzaDiscount.objects.all()}

def order(request):
	return {"order_list": Order.objects.all()}