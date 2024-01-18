from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE,related_name='seller',null = True,blank = True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic = models.ImageField(upload_to='product_pic/',blank=False,null=False)
    address = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    #offer
    #category
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name