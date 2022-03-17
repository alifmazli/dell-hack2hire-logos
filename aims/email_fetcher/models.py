from pickle import TRUE
from django.db import models

class Company (models.Model):
    company_id = models.IntegerField(primary_key=TRUE)
    company_name = models.CharField(max_length=200)
    company_email = models.EmailField

    def __str__(self):
        return self.company_name

class Product (models.Model):
    product_id =  models.IntegerField(primary_key = TRUE)
    product_name = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name

class Inventory (models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True)
    last_updated = models.DateField(auto_now=TRUE)