from django.urls import path
from . import views


urlpatterns = [path('', views.store, name = 'store'),
               

#cart/checkout stuff
path('cart/', views.cart, name = 'cart'),
path('add-to-cart/', views.add_to_cart, name = "add-to-cart"),
path('checkout/', views.checkout, name= 'checkout'),


#product view
path('product/<pid>/', views.product_detail, name= 'product'),

#posting
path("posting/", views.add_posting, name = 'posting')
]