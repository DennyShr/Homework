from django.urls import path
from .views import DrinksList

urlpatterns = [
	path('', DrinksList.as_view()),
	]