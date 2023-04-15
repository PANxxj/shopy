from django.shortcuts import render,get_object_or_404
from .models import Product



def detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    return render(request,'product/detail.html',{'product':product})