from django.urls import path
from .views import PizzasList, PizzaTemplateView, MyView, PizzaAddView, PizzaNameUpdate, PizzaChangePrice, FilterView, PizzasListFiltered

urlpatterns = [
	path('pizzas/', PizzasList.as_view()),
	path('', PizzaTemplateView.as_view()),
	path('view/', MyView.as_view()),
	path('pizzaadd/', PizzaAddView.as_view()),
	path('pizzaadd/<int:pk>/edit/', PizzaNameUpdate.as_view()),
	path('pizzaadd/<int:pk>/editprice/', PizzaChangePrice.as_view()),
	path('pizzas/filter=<str:fil>/', PizzasListFiltered.as_view()),
	path('pizzas/filter/', FilterView.as_view()),
]