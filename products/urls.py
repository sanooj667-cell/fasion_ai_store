from django.urls import path

from products import views
from .views import product_detail, product_list

urlpatterns = [
    path('', product_list),

    path('product_detail/<int:pk>/', views.product_detail, name='product-detail'),
]
