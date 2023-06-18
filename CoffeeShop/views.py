from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json

from .models import *

# Create your views here.

# CUSTOMERS


@api_view(['GET'])
def GetCustomers(request):
    CustomersList = Customers.objects.all()

    data = []
    for Customer in CustomersList:
        userData = {
            'CustomerID': Customer.id,
            'FirsName': Customer.FirstName,
            'LastName': Customer.LastName,
            'Email': Customer.Email,
            'PhoneNumber': Customer.PhoneNumber,
            'Address': Customer.Address,
            'City': Customer.City,
            'State': Customer.State,
            'PostalCode': Customer.PostalCode,
            'Password': Customer.Password
        }
        data.append(userData)

    return JsonResponse({'Customers': data})


@api_view(['POST'])
def SignUpCustomers(request):
    firstName = request.POST.get('FirstName')
    lastName = request.POST.get('LastName')
    email = request.POST.get('Email')
    phoneNumber = request.POST.get('PhoneNumber')
    address = request.POST.get('Address')
    city = request.POST.get('City')
    state = request.POST.get('State')
    postalCode = request.POST.get('PostalCode')
    password = request.POST.get('Password')

    Customers.objects.create(
        FirstName=firstName,
        LastName=lastName,
        Email=email,
        PhoneNumber=phoneNumber,
        Address=address,
        City=city,
        State=state,
        PostalCode=postalCode,
        Password=password
    )

    return Response({'status': 'ok'})


@api_view(['DELETE'])
def DeleteCustomer(request):
    CustomerID = request.POST.get('ID')
    Customers.objects.get(id=CustomerID).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def UpdateCustomer(request):
    customerID = request.POST.get('ID')
    firstName = request.POST.get('FirstName')
    lastName = request.POST.get('LastName')
    email = request.POST.get('Email')
    phoneNumber = request.POST.get('PhoneNumber')
    address = request.POST.get('Address')
    city = request.POST.get('City')
    state = request.POST.get('State')
    postalCode = request.POST.get('PostalCode')
    password = request.POST.get('Password')

    customer = Customers.objects.get(id=customerID)

    customer.FirstName = firstName
    customer.LastName = lastName
    customer.Email = email
    customer.PhoneNumber = phoneNumber
    customer.Address = address
    customer.City = city
    customer.State = state
    customer.PostalCode = postalCode
    customer.Password = password

    customer.save()

    return JsonResponse({'status': 'ok'})


# PRODUCTS
@api_view(['GET'])
def GetProducts(request):
    ProductsList = Products.objects.select_related('CategoryID').all()

    data = []
    for Product in ProductsList:
        productData = {
            'ProductID': Product.id,
            'ProductName': Product.ProductName,
            'Description': Product.Description,
            'Price': str(Product.Price),
            'Image': Product.Image,
            'CategoryID': Product.CategoryID.id,
            'CategoryName': Product.CategoryID.CategoryName
        }
        data.append(productData)

    return JsonResponse({'Products': data}, safe=False)


@api_view(['POST'])
def CreateProduct(request):
    productName = request.POST.get('ProductName')
    description = request.POST.get('Description')
    price = request.POST.get('Price')
    image = request.POST.get('Image')
    categoryID = request.POST.get('CategoryID')

    category = Categories.objects.get(id=categoryID)

    Products.objects.create(
        ProductName=productName,
        Description=description,
        Price=price,
        Image=image,
        CategoryID=category
    )

    return Response({'status': 'ok'})


@api_view(['DELETE'])
def DeleteProduct(request):
    ProductID = request.POST.get('ID')
    Products.objects.get(id=ProductID).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def UpdateProduct(request):
    productID = request.POST.get('ID')
    productName = request.POST.get('ProductName')
    description = request.POST.get('Description')
    price = request.POST.get('Price')
    image = request.POST.get('Image')
    categoryID = request.POST.get('CategoryID')

    Product = Products.objects.get(id=productID)
    Catetory = Categories.objects.get(id=categoryID)

    Product.ProductName = productName
    Product.Description = description
    Product.Price = price
    Product.Image = image
    Product.CategoryID = Catetory

    Product.save()

    return JsonResponse({'status': 'ok'})

# CATEGORIES


@api_view(['GET'])
def GetCategory(request):
    CategoriesList = Categories.objects.all()

    data = []
    for Category in CategoriesList:
        categoryData = {
            "CategoryID": Category.id,
            "CategoryName": Category.CategoryName,
            "CategoryDescription": Category.CategoryDescription,
            "CategoryImage": Category.CategoryImage
        }
        data.append(categoryData)

    return JsonResponse({'Categories': data})


@api_view(['POST'])
def CreateCategory(request):
    categoryName = request.POST.get('CategoryName')
    categoryDescription = request.POST.get('CategoryDescription')
    categoryImage = request.POST.get('CategoryImage')

    Categories.objects.create(
        CategoryName=categoryName,
        CategoryDescription=categoryDescription,
        CategoryImage=categoryImage
    )

    return JsonResponse({'status': 'ok'})


@api_view(['DELETE'])
def DeleteCategory(request):
    CategoryID = request.POST.get('ID')

    Categories.objects.get(id=CategoryID).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def UpdateCategory(request):
    categoryID = request.POST.get('ID')
    categoryName = request.POST.get('CategoryName')
    categoryDescription = request.POST.get('CategoryDescription')
    categoryImage = request.POST.get('CategoryImage')

    Category = Categories.objects.get(id=categoryID)

    Category.CategoryName = categoryName
    Category.CategoryDescription = categoryDescription
    Category.CategoryImage = categoryImage

    Category.save()

    return JsonResponse({'status': 'ok'})

# ORDERS


@api_view(['GET'])
def GetOrders(request):
    OrderList = Orders.objects.all()

    data = []
    for Order in OrderList:
        orderData = {
            'OrderID': Order.id,
            'CustomerOrder': Order.CustomerOrder_id,
            'OrderDate': str(Order.OrderDate),
            'TotalAmount': str(Order.TotalAmount),
            'PaymentType': Order.PaymentType,
            'Status': Order.Status
        }
        data.append(orderData)

    return JsonResponse({'data': data})


@api_view(['POST'])
def CreateOrder(request):
    # JSON
    JsonObject = json.loads(request.POST.get('Cart'))

    customerOrder = request.POST.get('CustomerOrder')
    orderDate = request.POST.get('OrderDate')
    totalAmount = request.POST.get('TotalAmount')
    paymentType = request.POST.get('PaymentType')
    status = request.POST.get('Status')

    Customer = Customers.objects.get(id=customerOrder)
    order = Orders.objects.create(
        CustomerOrder=Customer,
        OrderDate=orderDate,
        TotalAmount=totalAmount,
        PaymentType=paymentType,
        Status=status
    )

    # create OrderDetails field
    LatestOrder = Orders.objects.latest('id')
    LastOrderID = LatestOrder.id

    for product in JsonObject:
        Product_ID = product.get("ID")
        Product = Products.objects.get(id=Product_ID)

        OrderDetails.objects.create(
            OrderID=order,
            ProductID=Product,
            Quantity=product.get("Count"),
            ItemNotes=None,
            ItemPrice=product.get("Price"),
            ItemDiscount="0",
            ItemTotal=product.get("TotalAmount"),
            ItemStatus=status
        )

    return JsonResponse({'status': 'ok'})


@api_view(['DELETE'])
def DeleteOrder(request):
    OrderID = request.POST.get('ID')

    Orders.objects.get(id=OrderID).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def UpdateOrder(request):
    orderID = request.POST.get('ID')
    customerOrder = request.POST.get('CustomerOrder')
    orderDate = request.POST.get('OrderDate')
    totalAmount = request.POST.get('TotalAmount')
    paymentType = request.POST.get('PaymentType')
    status = request.POST.get('Status')

    Customer = Customers.objects.get(id=customerOrder)
    Order = Orders.objects.get(id=orderID)

    Order.CustomerOrder = Customer
    Order.OrderDate = orderDate
    Order.TotalAmount = totalAmount
    Order.PaymentType = paymentType
    Order.Status = status

    Order.save()

    return JsonResponse({'status': 'ok'})

# ORDERDETAILS


@api_view(['GET'])
def GetOrderDetails(request):
    orderDetailsID = request.POST.get('ID')
    OrderDetailsList = OrderDetails.objects.filter(
        OrderID_id=orderDetailsID).select_related('ProductID')

    data = []
    for OrderDetaile in OrderDetailsList:
        orderDetaileData = {
            'OrderID': OrderDetaile.OrderID_id,
            'ProductID': OrderDetaile.ProductID_id,
            'ProductName': OrderDetaile.ProductID.ProductName,
            'Quantity': OrderDetaile.Quantity,
            'ItemNotes': OrderDetaile.ItemNotes,
            'ItemPrice': OrderDetaile.ItemPrice,
            'ItemDiscount': OrderDetaile.ItemDiscount,
            'ItemTotal': OrderDetaile.ItemTotal,
            'ItemStatus': OrderDetaile.ItemStatus
        }
        data.append(orderDetaileData)

    return JsonResponse({'OrderDetails': data})


@api_view(['PUT'])
def UpdateOrderDetails(request):
    # Json
    JsonObject = json.loads(request.POST.get('Cart'))

    status = request.POST.get('Status')
    OrderID = request.POST.get('ID')
    customerOrder = request.POST.get('CustomerOrder')

    # Get Parent Objects
    Order = Orders.objects.get(id=OrderID)
    Customer = Customers.objects.get(id=customerOrder)

    # DELETE all RECORD related to OrderID
    OrderDetails.objects.filter(OrderID_id=OrderID).delete()

    TotalFactor = 0
    for product in JsonObject:
        # Get Parent Object
        Product_ID = product.get("ID")
        Product = Products.objects.get(id=Product_ID)

        TotalPrice = product.get("TotalAmount")

        OrderDetails.objects.create(
            OrderID=Order,
            ProductID=Product,
            Quantity=product.get("Count"),
            ItemNotes=None,
            ItemPrice=product.get("Price"),
            ItemDiscount="0",
            ItemTotal=TotalPrice,
            ItemStatus=status
        )

        TotalFactor += int(TotalPrice)

    # set totalAmount & status to order table
    Order.CustomerOrder = Customer
    Order.TotalAmount = TotalFactor
    Order.Status = status
    Order.save()

    return JsonResponse({'status': 'ok'})
