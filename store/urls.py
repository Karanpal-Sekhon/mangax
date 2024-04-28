from django.urls import path
from . import views


urlpatterns = [path('', views.store, name = 'store'),
               

#cart/checkout stuff
path('cart/', views.cart, name = 'cart'),
path('add-to-cart/', views.add_to_cart, name = "add-to-cart"),
path('checkout/', views.checkout, name= 'checkout'),


#search
path("search/", views.search_view, name = 'search'),

#product view
path('product/<pid>/', views.product_detail, name= 'product'),

#posting
path("posting/", views.add_posting, name = 'posting'),

#deleting from the cart
path('delete-from-cart', views.delete_from_cart, name='delete_from_cart')
]