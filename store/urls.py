from django.urls import path
from . import views


urlpatterns = [path('', views.store, name = 'store'),
               

#cart stuff
path('cart/', views.cart, name = 'cart'),
path('add-to-cart/', views.add_to_cart, name = "add-to-cart"),

path('checkout/', views.checkout, name= 'checkout'),
path('product/<pid>/', views.product_detail, name= 'product'),
]