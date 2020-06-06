from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class  MonthlyBills(models.Model):
    description = models.CharField(max_length=2200, null=True)
    price = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateField(default=timezone.now, blank=True)
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.description
    

    #default ordering
    class Meta:
        ordering = ['-id']
   


