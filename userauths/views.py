from django.shortcuts import render

# Create your views here.


def register_view(request):
    return render(request, "store/templates/signup.html")