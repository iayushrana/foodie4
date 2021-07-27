from django.shortcuts import render,redirect
from .models import OrderItem,Order
from .forms import OrderCreateForm
from food.cart import Cart
from django.contrib.auth.decorators import login_required
from orders.models import Order
from decimal import Decimal
from django.shortcuts import get_object_or_404



@login_required(login_url='/login_user')
def order_create(request):
        cart = Cart(request)
        a=0
        for item in cart:
            a=a+1

        if  a != 0 :
            if request.method == 'POST':
                form = OrderCreateForm(request.POST)
                if form.is_valid():
                    order = form.save()
                    order.user=request.user
                    order.total_cost=sum(Decimal(item['price']) * item['quantity'] for item in cart)

                    for item in cart:
                        OrderItem.objects.create(
                            order=order,
                            product=item['product'],
                            price=item['price'],
                            quantity=item['quantity'],
                            total_i_price=item['price']*item['quantity']
                        )
                    cart.clear()
                order.save()
                return render(request, 'orders/order/created.html', {'order': order})


            else:
                form = OrderCreateForm()
            return render(request, 'orders/order/create.html', {'form': form})
        else:
            return redirect('food:cart_detail')


@login_required(login_url='/login_user')
def your_order(request):
    orders = Order.objects.filter(user=request.user)
    ialbum = get_object_or_404(Order, pk=2)

    order_items=OrderItem.objects.all()
    return render(request,'orders/order/your_order.html', {'orders':orders,'ialbum':ialbum ,'order_items':order_items})

@login_required(login_url='/login_user')
def order_created(request):
    return render(request, 'orders/order/created.html')
