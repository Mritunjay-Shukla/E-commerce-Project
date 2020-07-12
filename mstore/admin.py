from django.contrib import admin
from mstore.models import Product, Cart, Order, Category, Item, CIM, OIM, Review
# Register your models here.
 
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(CIM)
admin.site.register(OIM)
admin.site.register(Review)


