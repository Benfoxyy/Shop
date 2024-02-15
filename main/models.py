from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE,related_name='seller',null = True,blank = True)
    name = models.CharField(max_length=255)
    Category = models.ManyToManyField(Category,blank = False, null = True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic = models.ImageField(upload_to='product_pic/',blank=False,null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=12)
    #offer
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:single',kwargs={'pk':self.id})
    
class Wishlist(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    wished_items = models.ManyToManyField(Product,blank=True,null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.users.username