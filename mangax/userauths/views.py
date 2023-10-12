from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


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