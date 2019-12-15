from django.urls import path
from .views import OrderCreateView, DishesCountView, ChangeOrder, ChangeCountForm

urlpatterns = [
path('add/', OrderCreateView.as_view(), name='order-add'),
path('add/order<int:pk>/', DishesCountView.as_view()),
path('add/order<int:pk>_<int:name>/change_count/', ChangeCountForm.as_view()),
path('edit_order_<int:pk>/', ChangeOrder.as_view()),
]