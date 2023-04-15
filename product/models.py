from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name=models.CharField(max_length=225)
    
    class Meta:
        ordering=('name',)
        
    def __str__(self) -> str:
        return self.name  
        
class Product(models.Model):
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    is_sold=models.BooleanField(default=False)
    image=models.ImageField(upload_to="product_image",blank=True,null=True)
    created_by=models.ForeignKey(User,related_name='product',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    
