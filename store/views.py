from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse # returns message
from .models import *
from store.models import Product, CartOrder, CartOrderItems, Category, Address, WishList, ProductImages

# Create your views here.

def store(request):
    product = Product.objects.all().order_by("-id")
    categories = Category.objects.all()

    context = {
        "products": product,
        "categories": categories
    }


    # context = {'products': products}
    return render(request, 'store/store.html', context)




def product_detail(request, pid):
    product = Product.objects.get(pid = pid)
    # product = get_object_or_404(Product, )

    context = {
        "product" : product
    }

    return render(request, "store/productview.html", context)



    
def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['pid'])] = {
        'title': request.GET['title'],
        'price': request.GET['price'],
        'image': request.GET['image']
    }

    if 'cart_data_obj' in request.session:
        cart_data = request.session['cart_data_obj']
        cart_data.update(cart_product)
        request.session['cart_data_obj'] = cart_data

    else:
        request.session['cart_data_obj'] = cart_product
    
    return JsonResponse({"data": request.session['cart_data_obj'], "total_cart_items": len(request.session['cart_data_obj'])})



def get_cart_total(request):
    total = 0
    count = 0
    if 'cart_data_obj' in request.session:
        cart_data = request.session['cart_data_obj']
        for product_id, product_info in cart_data.items():
            count+=1
            total += float(product_info['price'])  # Convert price to a float and add to the total
        return total, count
    else:
        return total, count


    
def cart(request):


    
    price_total, item_total = get_cart_total(request)

    context = {
        "price_total": price_total,
        "item_total": item_total
    }
    return render(request, 'store/cart.html', context)

    
def checkout(request):
    price_total, item_total = get_cart_total(request)

    context = {
        "price_total": price_total,
        "item_total": item_total
    }

    return render(request, 'store/checkout.html', context)


