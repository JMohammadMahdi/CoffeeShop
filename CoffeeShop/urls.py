from django.urls import path
from . import views

# URLConf

# Dufalt URL = "coffeeshop/"
urlpatterns = [
    # Custoemrs
    path('get-customers/', views.GetCustomers),
    path('signup-customer/', views.SignUpCustomers),
    path('delete-customer/', views.DeleteCustomer),
    path('update-customer/', views.UpdateCustomer),
    # Product
    path('get-products/', views.GetProducts),
    path('create-product/', views.CreateProduct),
    path('delete-product/', views.DeleteProduct),
    path('update-product/', views.UpdateProduct),
    # Category
    path('get-category/', views.GetCategory),
    path('create-category/', views.CreateCategory),
    path('delete-category/', views.DeleteCategory),
    path('update-category/', views.UpdateCategory),
    # Orders
    path('get-orders/', views.GetOrders),
    path('create-order/', views.CreateOrder),
    path('delete-order/', views.DeleteOrder),
    path('update-order/', views.UpdateOrder),
    # OrderDetails
    path('get-orderdetails/', views.GetOrderDetails),
    path('update-orderdetails/', views.UpdateOrderDetails),
]
