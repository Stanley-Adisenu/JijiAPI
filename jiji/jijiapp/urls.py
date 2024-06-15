from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.getProducts ),
    path('products/<int:pk>/', views.getProduct ),
    path('carts/', views.cartList ),
    path('carts/<int:pk>/', views.updateCart ),
    path('quantity/<int:pk>/', views.getStock ),
    path('addcart/', views.createCart ),
]