from django.urls import path
from . views import start_order
from core.views import myaccount

app_name='order'

urlpatterns=[
    path('',start_order,name='start_order'),
    
]