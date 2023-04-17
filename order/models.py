from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    ORDERED='ordered'
    SHIPPED='shipped'

    STATUS_CHOICES = (
        (ORDERED,'Orederd'),
        (SHIPPED,'Shipped')
    )
    user=models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    email=models.EmailField()
    address=models.CharField(max_length=225)
    pincode=models.PositiveIntegerField()
    phone=models.PositiveIntegerField()
    place=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    paid=models.BooleanField(default=False)
    paid_amount=models.IntegerField(blank=True,null=True)

    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=ORDERED)
    
    
    
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)

    