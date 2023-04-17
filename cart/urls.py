from django.urls import path
from . import views

app_name='cart'


urlpatterns=[
    path('',views.cart,name='cart'),
    path('checkout/',views.check_out,name='checkout'),
    path('update_cart/<int:product_id>/<str:action>/',views.update_cart,name='update_cart'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('hx_menu_cart/',views.hx_menu_cart,name='hx_menu_cart'),
    path('hx_cart_total/',views.hx_cart_total,name='hx_cart_total')
]