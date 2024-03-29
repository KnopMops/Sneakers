from django.urls import path
from .views import *

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view(), name='latest-products'),
    path('products/search/', search, name='search'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product-detail'),
    path('products/<slug:category_slug>/', CategoryDetail.as_view(), name='category-detail')
]