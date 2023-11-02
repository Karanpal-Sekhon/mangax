from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from .models import User
# from django.conf import settings
# Create your views here.

# User = settings.AUTH_USER_MODEL

def signup(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created succesfully")
            new_user = authenticate(username = form.cleaned_data['email'], password = form.cleaned_data["password1"])
            
            login(request, new_user)

            return redirect("store")

    else:
        form = UserRegisterForm()

    context = {"form": form}
    return render(request, "userauths/signup.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey you are already logged in!")
        return redirect("store")


    if request.method == "POST":
        email = request.POST.get("email") # GETS EMAIL THAT USER INPUTS
        password = request.POST.get("password") # GETS PASSWORD THAT USER INPUTS

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exist")

        user = authenticate(request, email=email, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in.")
            return redirect("store")
        else:
            messages.warning(request, f"user does not exist. Create an account")
    
    context = {}

    return render(request, "userauths\login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("userauths:signup")


def account_view(request):


    if request.method == "POST":
        # GET THE USER
        user = request.user

        # SET FIRST AND LAST NAMES
        fullname = request.POST.get("name")
        user.first_name = fullname.split()[0]
        user.last_name = fullname.split()[1]
        

        # SET USERNAME
        user_name = request.POST.get("username")
        user.username= user_name

        # SET DESCRIPTION
        description = request.POST.get("description")
        user.description = description

        # SAVE USER CHANGES
        user.save()

        messages.success(request, "User Successfully updated")

    context = {}
    return render(request, 'userauths/account.html', context)
    
def wishlist_view(request):

    context = {}
    return render(request, "userauths\wishlist.html", context)