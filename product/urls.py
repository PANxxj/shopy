from django.urls import path
from .import views

app_name='product'

urlpatterns=[
    # path('',views.product,name='product'),
    path('<int:pk>/',views.detail,name='detail')
]