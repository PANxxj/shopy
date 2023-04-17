from django.shortcuts import render,redirect
from .models import Order,OrderItem
from cart.cart import Cart

def start_order(request):
    cart=Cart(request)
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        place=request.POST.get('place')
        pincode=request.POST.get('pincode')
        phone=request.POST.get('phone')
        
        order=Order.objects.create(user=request.user,first_name=first_name,last_name=last_name,email=email,address=address,pincode=pincode,phone=phone,place=place)

        for item in cart:
            product=item['product']
            quantity=int(item['quantity'])
            price=product.price*quantity

            item=OrderItem.objects.create(order=order,product=product,price=price,quantity=quantity)
        return redirect('account')
    return redirect('cart')
