from django.contrib import admin
from store.models import Product, CartOrder, CartOrderItems, Category, Address, WishList, ProductImages
# Register your models here.




from .models import * 


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'product_image', 'price', 'featured', 'pid']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']


# class VendorAdmin(admin.ModelAdmin):
#     list_display = ['title', 'vendor_image']
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', "order_date", "product_status"]

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'price', 'total']

class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']
    

admin.site.register(Product, ProductAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Address, AddressAdmin)
# admin.site.register(Vendor, VendorAdmin)
admin.site.register(WishList, wishlistAdmin)









# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(ShippingAddress)
