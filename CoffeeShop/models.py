from django.db import models

# Create your models here.


class Categories(models.Model):
    CategoryName = models.CharField(max_length=255)
    CategoryDescription = models.CharField(max_length=255, null=True)
    CategoryImage = models.TextField(max_length=255, null=True)


class Products(models.Model):
    ProductName = models.CharField(max_length=50)
    Description = models.TextField(null=True)
    Price = models.DecimalField(max_digits=20, decimal_places=2)
    Image = models.TextField(null=True)
    CategoryID = models.ForeignKey(
        'Categories', on_delete=models.PROTECT)


class Customers(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True, max_length=100)
    PhoneNumber = models.CharField(max_length=20, null=True)
    Address = models.CharField(max_length=200, null=True)
    City = models.CharField(max_length=20, null=True)
    State = models.CharField(max_length=50, null=True)
    PostalCode = models.CharField(max_length=20, null=True)
    Password = models.CharField(max_length=255, default=None)


class Orders(models.Model):
    CustomerOrder = models.ForeignKey(
        'Customers', on_delete=models.PROTECT, related_name='orders')
    OrderDate = models.CharField(max_length=20)
    TotalAmount = models.DecimalField(max_digits=20, decimal_places=0)
    PaymentType = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)


class OrderDetails(models.Model):
    OrderID = models.ForeignKey(
        'Orders', on_delete=models.PROTECT)
    ProductID = models.ForeignKey(
        'Products', on_delete=models.PROTECT)
    Quantity = models.CharField(max_length=20)
    ItemNotes = models.CharField(max_length=255, null=True, blank=True)
    ItemPrice = models.CharField(max_length=255, default=None)
    ItemDiscount = models.CharField(max_length=3, default=None)
    ItemTotal = models.DecimalField(max_digits=20, decimal_places=0)
    ItemStatus = models.CharField(max_length=20, default=None)
