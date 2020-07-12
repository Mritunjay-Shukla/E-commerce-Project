from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=20000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    new_arrival = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.product, self.quantity)


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return "cart of {}" .format(self.user)

class CIM(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    shipment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "order for {}".format(self.user)

class OIM(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    review = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=5)