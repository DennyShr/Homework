from django.urls import path
from .views import PizzasList, PizzaTemplateView, MyView, PizzaAddView

urlpatterns = [
	path('pizzas/', PizzasList.as_view()),
	path('', PizzaTemplateView.as_view()),
	path('view/', MyView.as_view()),
	path('pizzaadd/', PizzaAddView.as_view()),
]