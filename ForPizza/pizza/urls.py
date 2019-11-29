from django.urls import path
from .views import PizzasList, PizzaTemplateView, MyView, FeedbackView, PizzaOrderCreate

urlpatterns = [
	path('pizzas/', PizzasList.as_view()),
	path('', PizzaTemplateView.as_view()),
	path('view/', MyView.as_view()),
	path('pizza_order/add/', PizzaOrderCreate.as_view(), name='order-add'),
	path('feedback/', FeedbackView.as_view()),
]