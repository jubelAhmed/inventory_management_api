from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    note = models.TextField(max_length=500,null=True,blank=True)
    stock = models.IntegerField(default=0)    
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name