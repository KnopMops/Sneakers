from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('orders/', OrdersList.as_view(), name='orders')
]