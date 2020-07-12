from django.shortcuts import render
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from mstore.models import Product, Category, Cart, Item, Order, CIM, OIM, Review
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from account.models import User
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from json import dumps
from django.core import serializers
from django.template import RequestContext
from django.db.models import Aggregate, Avg

# Create your views here.
def homepage(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, "home.html", context={'product':product, "category":category})

def product_detail(request, id):
    product = Product.objects.get(id = id)
    similar_product = Product.objects.filter(category = product.category)
    rating = Review.objects.filter(product=product)
    print(rating)
    if rating:
        l = []
        for rat in rating:
            l.append(rat.rating)
        tr = len(l)
        gr = sum(l)
        fr = gr/tr
        return render(request, "proddetail.html", context={'product':product, 'similar_product':similar_product, 'fr':fr})
    else:
        return render(request, "proddetail.html", context={'product':product, 'similar_product':similar_product})


def category(request, category):
    product = Product.objects.filter(category = category)
    return render(request, "categoryhome.html", context={'product':product})

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        product = Product.objects.filter(
        Q(name__icontains = search,)|
        Q(description__icontains = search,)
        )
        return render(request, "search.html", context={'product':product})

def addcart(request, **kwargs):
    quantity = request.POST.get('quantity')
    product = Product.objects.get(id=kwargs.get('id'))
    items = Item.objects.create(product = product, quantity=quantity)
    session_item = Item.objects.filter(id = items.id)
    if request.user.is_authenticated:
        cart_qs = Cart.objects.get_or_create(user=request.user)
        CIM.objects.create(user=request.user,item=items, cart=cart_qs[0])
        return redirect('/')
    else:
        #cart = request.session['cart']
        if not request.session.get('cart'):
            request.session['cart'] = serializers.serialize('json', {product:quantity})
            #print(request.session.get('cart'))
        else:
            request.session['cart'] += serializers.serialize('json', {product:quantity})
            #print(request.session.get('cart'))
        #cart_item = request.session.get('cart')
        #request.session['cart'] = {product:quantity}
        cart_items = Product.objects.filter(id = kwargs.get('id'))
        print(cart_items)
        quantity = request.POST.get('quantity')
        #total = cart_items[0]*quantity
        #print(request.session['cart'])
        return render(request, 'scart.html', context={'cart_items':cart_items, ' quantity':quantity})
    
def viwcart(request):
    cart_items = CIM.objects.filter(user__username = request.user)
    l = []

    for prod in cart_items:
        quantity=prod.item.quantity
        price = prod.item.product.price
        p = quantity*price
        l.append(p)
    total = sum(l)
    if request.user.is_authenticated:
        return render(request, 'cart.html', context={"cart_items":cart_items, 'total':total})
    else:
        pass

def palceorder(request, **kwargs):
    print(kwargs)
    cim = CIM.objects.filter(user__username = request.user)
    cims = []
    for i in cim:
        a = i.item.product.name
        cims.append(a)
    order = Order.objects.get_or_create(user=request.user)
    items = Item.objects.filter(cim__user__username= request.user)
    for i in items:
        OIM.objects.create(item = i, order = order[0])
    cim.delete()
    print(items)
    print(kwargs)
    return render(request, 'order.html', context={'cims':cims})

def addreview(request, **kwargs):
    rating = request.POST.get('rating')
    review_sms = request.POST.get('review')
    product = Product.objects.get(id=kwargs.get('id'))
    print(product)
    print(rating)
    print(review_sms)
    review = Review.objects.create(product = product, review = review_sms, user = request.user, rating= rating)
    return redirect('/')

    
    




