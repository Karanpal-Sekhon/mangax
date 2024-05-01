from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse # returns message
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import *
from store.models import Product, CartOrder, CartOrderItems, Category, Address, WishList, ProductImages
from django.template.loader import render_to_string
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

    context = {
        "product" : product
    }

    return render(request, "store/productview.html", context)


def add_posting(request):

    if request.method == "POST":
        title = request.POST.get("product-title")
        category = request.POST.get("product-category")

        category = Category.objects.get(title = category)
        description = request.POST.get("product-description")
        price = request.POST.get("product-price")
        image = request.FILES.get("product-image")


        image_name = f"user_{request.user.id}/{image.name}"
        default_storage.save(image_name, ContentFile(image.read()))

        
        product = Product(
            title=title,
            category = category,
            description=description,
            price=price,
            image=image_name,
            user=request.user  # Associate the product with the current user
        )

        product.save()

        
        messages.success(request, "Your posting has been added!", extra_tags="posting_update")

        return redirect('product', pid = product.pid)


    context = {}

    return render(request, "store/posting.html/", context)



    
def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['pid'])] = {
        'title': request.GET['title'],
        'price': request.GET['price'],
        'image': request.GET['image']
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET["pid"]) in request.session["cart_data_obj"]:
            pass # do not add to the cart if product already in there, in future send message saying product already in cart
        else:
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


    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")
        country = request.POST.get("country")


        print(name, email, address, city, state, zipcode, country)

        return redirect("store")


    context = {
        "price_total": price_total,
        "item_total": item_total
    }

    return render(request, 'store/checkout.html', context)


def search_view(request):
    query = request.GET["q"]

    print(query)

    products = Product.objects.filter(title__icontains = query, description__icontains = query).order_by("-date")
    context = {
        "products": products,
        "query": query
    }

    return render(request, 'store/search.html', context)



def category_view(request, category_name):
    # Get the Category object by its title
    category = get_object_or_404(Category, title=category_name)

    # Get the products related to this category
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'category_name': category.title,  # Use the Category's title to be consistent
        'products': products
    }

    return render(request, 'store/category.html', context)



def delete_from_cart(request):
    product_id = str(request.GET["id"])
    if 'cart_data_obj' in request.session:
        if product_id in request.session["cart_data_obj"]:
            del request.session['cart_data_obj'][product_id]

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += float(item['price'])
        
    context = render_to_string("store/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], "totalcartitems": len(request.session["cart_data_obj"]), 'cart_total_amount':cart_total_amount}) 
    return JsonResponse({"data": context, "totalcartitems": len(request.session["cart_data_obj"])})








