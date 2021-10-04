from django.urls import path
from .import views


urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('sample-list/',views.sampleList, name="sample-list"),
    path('sample-create/',views.sampleCreate, name="sample-create"),
    path('sample-detail/<str:pk>/',views.sampleDetail, name="sample-detail"),
    path('sample-update/<str:pk>/',views.sampleUpdate, name="sample-update"),
    path('customer-first/',views.customerFirstOrLast, name="customer-first"),
    path('customer-byname/<str:name>/',views.customerByName, name="customer-byname"),
    path('first-customer-orders/',views.firstCustomerOrders, name="first-customer-orders"),
    path('first-order-customername/',views.customerNameOfFirstOrder, name="first-order-customername"),
    path('order-bycategory/',views.orderByCategory, name="order-bycategory"),
    path('product-bytags/',views.productByTags, name="product-bytags"),
    path('ordercount-product/',views.todalCountForEachProduct, name="ordercount-product"),
]