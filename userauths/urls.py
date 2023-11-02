from django.urls import path

from userauths import views

app_name = "userauths"

urlpatterns = [
    path("signup/", views.signup, name = "signup"),
    path("login/", views.login_view, name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("account/", views.account_view, name="account_view"),
    path("wishlist/", views.wishlist_view, name="wishlist")
    
]