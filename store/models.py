from django.db import models
from django.conf import settings
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique = True, length = 10, max_length = 20, prefix = "cat", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100, default="Category Title")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src = "%s" width = "50" height = "50" />' % (self.image.url))
       
    def __str__(self):
        return self.title
    

class Tags(models.Model):
    pass
    


# class Vendor(models.Model):
#     vid = ShortUUIDField(unique = True, length = 10, max_length = 20, prefix = "ven", alphabet = "abcdefgh12345")


#     title = models.CharField(max_length=100, default="Vendor Title")
#     image = models.ImageField(upload_to=user_directory_path, default= "vendor.jpg")
#     description = models.TextField(null=True, blank=True, default="Vendor Description")



#     address = models.CharField(max_length=100, default="123 Main Street")
#     contact = models.CharField(max_length=100, default = "+123 (456) 789")
    
#     authentic_rating = models.CharField(max_length=100, default = "100")


#     user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

#     class Meta:
#         verbose_name_plural = "Vendors"

#     def vendor_image(self):
#         return mark_safe('<img src = "%s" width = "50" height = "50" />' % (self.image.url))
    
#     def __str__(self):
#         return self.title
    


class Product(models.Model):
    pid = ShortUUIDField(unique = True, length = 10, max_length = 20, prefix = "prd", alphabet = "abcdefgh12345", null=True)


    title = models.CharField(max_length=100, default="Product Title")
    image = models.ImageField(upload_to=user_directory_path, default= "product.jpg")
    description = models.TextField(null=True, blank=True, default="Product Description")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    specifications = models.TextField(null=True, blank=True, default="Product Specifications")
    #tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True, default=None)


    featured = models.BooleanField(default=False) 
    sku = ShortUUIDField(unique = True, length = 4, max_length = 10, prefix = "sku", alphabet = "1234567890")

    date = models.DateTimeField(auto_now_add=True, null=True)

    updated = models.DateTimeField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src = "%s" width = "50" height = "50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class ProductImages(models.Model):
    images = models.ImageField(upload_to = "produt-images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

    
#################################### Cart, Order, OrderItems ###################################

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999999999999, decimal_places=2, default="0.00")
    product_status = models.CharField(max_length=200)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Cart Order"

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9999999999999999999, decimal_places=2, default="0.00")
    total = models.DecimalField(max_digits=9999999999999999999, decimal_places=2, default="0.00")

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_img(self):
        return mark_safe('<img src = "%s" width = "50" height = "50" />' % (self.image))
    

#################################### Wishlist, Address #####################################

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wishlists"

    def __str__(self):
        return self.product.title
    

class Address(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null = True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"





 
# class Product(models.Model):
#     pid = ShortUUIDField(unique = True, length = 10, max_length = 20, alphabet = "abcdefgh12345")
#     user = models.ForeignKey(User, on_delete= models.CASCADE)
#     category = models.ForeignKey(Category, on_delete = models.CASCADE)
#     name = models.CharField(max_length=200, null=True, default="Title")
#     price = models.FloatField()
#     digital = models.BooleanField(default=False, null = True, blank=False)
#     image = models.ImageField(null=True, blank=True)
#     description = models.TextField(max_length=1000, default="Product Description")
#     tags = models.ForeignKey(Tags, on_delete=models.CASCADE)



#     def __str__(self):
#         return self.name


#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ""
#         return url


















# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True) # user can only have one customer, customer can only have one user
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
    
#     def __str__(self):
#         return self.name

# class Order(models.Model):

#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank = True, null = True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     transaction_id = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return str(self.id)

#     @property
#     def get_cart_total(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.get_total for item in orderitems])
#         return total
#     @property
#     def get_cart_items(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.quantity for item in orderitems])
#         return total
#     @property
#     def shipping(self):
#         shipping = False
#         orderitems = self.orderitem_set.all()
#         for i in orderitems:
#             if i.product.digital == False:
#                 shipping = True
#             return shipping

    


# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank = True, null = True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank = True, null = True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     @property
#     def get_total(self):
#         total = self.product.price * self.quantity
#         return total
    
# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     address = models.CharField(max_length=200, null=True)
#     city = models.CharField(max_length=200, null=True)
#     state = models.CharField(max_length=200, null=True)
#     zip_code = models.CharField(max_length=200, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.address







