from django.shortcuts import render
from django.http import JsonResponse # returns message
from .models import *
import json
# Create your views here.

def store(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False) # creating object or querying one
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    #     items = []
    #     order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
    #     cartItems = order['get_cart_items']


    products = Product.objects.all()
    #context = {'products': products, 'cartItems': cartItems}


    context = {'products': products}
    return render(request, 'store/store.html', context)

    
def cart(request):

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False) # creating object or querying one
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    #     items = []
    #     order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
    #     cartItems = order['get_cart_items']
    # context = {"items":items, "order": order, 'cartItems': cartItems}

    context = {}
    return render(request, 'store/cart.html', context)

    
def checkout(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False) # creating object or querying one
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    #     items = []
    #     order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
    #     cartItems = order['get_cart_items']
    # context = {"items":items, "order": order, 'cartItems': cartItems}

    context = {}

    return render(request, 'store/checkout.html', context)


def productview(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False) # creating object or querying one
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    #     items = []
    #     order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
    #     cartItems = order['get_cart_items']
    # context = {"items":items, "order": order, 'cartItems': cartItems}

    context = {}
    return render(request, 'store/productview.html', context)



def updateItem(request):
    # data = json.loads(request.body)
    # productId = data["productId"]
    # action = data["action"]

    # print("Action:", action)
    # print("ProductId:", productId )


    # customer = request.user.customer
    # product = Product.objects.get(id=productId)
    # order, created = Order.objects.get_or_create(customer=customer, complete=False) # creating object or querying one

    # orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    # if action == 'add':
    #     orderItem.quantity +=1
    # elif action == 'remove':
    #     orderItem.quantity -=1

    # orderItem.save()

    # if orderItem.quantity <=0:
    #     orderItem.delete()


    return JsonResponse("Item was added", safe = False) # response
