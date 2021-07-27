from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.views.generic import View
from .models import Category,Product
from .cart import Cart
from django.template import loader
from django.db.models import Q
from django.views.decorators.http import require_POST

from food.forms import CartAddProductForm




def Vindex(request):
    album = get_object_or_404(Category, pk=2)
    cart_product_form = CartAddProductForm()
    # template = loader.get_template('music/index.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    return render(request, 'food/index.html', {'album': album, 'type':"vegetables", 'cart_product_form':cart_product_form})



def Findex(request):
    album = get_object_or_404(Category, pk=1)
    cart_product_form = CartAddProductForm()
    # template = loader.get_template('music/index.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    return render(request, 'food/index.html', {'album': album, 'type':"vegetables", 'cart_product_form':cart_product_form})



def detail(request, album_id):
    album = get_object_or_404(Product,pk=album_id)
    cart_product_form = CartAddProductForm()

    return render(request, 'food/detail.html', {'album': album ,'cart_product_form': cart_product_form})
    #in this we will get albumname_albumartist as becouse we done in models to give only title f album then doalbum.album_title




def sfood(request):
    category = Category.objects.all()
    product = Product.objects.all()
    template = loader.get_template('food/sfood.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care
    cart_product_form = CartAddProductForm()

    query = request.GET.get("q")
    if query:
        category = category.filter(
            Q(name__icontains=query) |
            Q(nick_names__icontains=query)
        ).distinct()

        product = product.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(nick_names__icontains=query) |
            Q(price__icontains=query)
        ).distinct()

        return render(request, 'food/sfood.html', {
            'category': category,
            'product': product,
            'cart_product_form': cart_product_form,
        })

    else:
        return render(request, 'food/sfood.html', {
            'category': category,
            'product': product,
            'cart_product_form': cart_product_form,
        })


def about_us(request):
    return render(request,'food/about.html',{'food':"ayush",})

def contact_us(request):
    return render(request,'food/about.html',{'food':"contact",})


'''
def cart_create(user=None):
    cart_obj=Cart.objects.create(user=None)
    print('new cart creted')
    return cart_obj

def cart_home(request):
    #del request.session['cart_id']
    request.session['cart_id']=int("12")#we set y default that d is thre whether it belongs to ue or not
    cart_id=request.session.get("cart_id",None)
#we are creatin
    # g nione user because to stor data of outsiders withoue loginuserrs

    if cart_id is None:# and isinstance(cart_id,int):
        cart_obj=cart_create()
        request.session['cart_id']=cart_obj.id
    else:
        qs=Cart.objects.filter(id=cart_id)#this means catr exist adn wherther t has data or nt it checks

        if qs.count()==1:#check thrt therr i s any cart daa or nto or its object
            print('cart id exist')
            cart_obj=qs.first()
        else:
            cart_obj=cart_create()#if threr is no data then create
            request.session['cart_id']=cart_obj.id#this taes the above id only


    return render(request,"food/carts.html",{})



'''


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('food:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('food:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    a=0
    message=''
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
        a+=1
    if a==0:
        message='Please Add item to the cart before shopping'
    return render(request, 'food/cart_detail.html', {'cart': cart,'message':message})

