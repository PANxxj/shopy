from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models import Product,Category
from .forms import SignupForm

# Create your views here.

def frontpage(request):
    product=Product.objects.all()[0:8]
    return render(request,'core/frontpage.html',{'product':product})

def shop(request):
    categories=Category.objects.all()
    product=Product.objects.all()
    
    active_cat=request.GET.get('category')
    return render(request,'core/shop.html',{'product':product,'categories':categories})


# Create your views here.
def product(request):
    query=request.GET.get('query','')
    product=Product.objects.filter(is_sold=False)
    
    if query:
        product=product.filter(name__icontains=query)
    return render(request,'product/detail.html',{'query':query,'product':product})
    
    
    
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
    else:
            form=SignupForm()
     
    return render(request,'core/signup.html',{'form':form})

@login_required
def myaccount(request):
    return render(request,'core/account.html')