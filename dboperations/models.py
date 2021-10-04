from django.db import models

# Create your models here.

class Sample(models.Model):
    sampleId = models.AutoField(primary_key=True)
    sampleName = models.CharField(max_length=100)
    sampleDateOfCreated = models.DateField()
    samplePhoto = models.CharField(max_length=50)

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)


class Tags(models.Model):
    name = models.CharField(max_length=100, null=True)    

class Product(models.Model):

    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        ('Sport','Sport',),
        ('Kitchen', 'Kitchen')
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tags)

class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out of Delivery', 'Out of Delivery'),
        ('Delivered', 'Delivered')
    )

    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
