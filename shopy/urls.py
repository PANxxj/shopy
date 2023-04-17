from django.conf.urls.static import static
from django .conf import settings
from django.contrib import admin
from django.urls import path,include
from cart.views import add_to_cart,cart

urlpatterns = [
    path('',include('core.urls')),
    path('order/',include('order.urls')),
    path('cart/',include('cart.urls')),
    path('product/',include('product.urls')),
    path('admin/', admin.site.urls),
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
