import re
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Customer, Order, Product, Sample, Tags
from .serializers import (CustomerSerializer, OrderSerializer,
                          ProductSerializer, SampleSerializer, TagsSerializer)

# Create your views here.


def apiOverview(request):
    api_urls = {
        'List':'/sample-list/',
        'Detail':'/sample-detail/<str:pk>/',
        'Create':'/sample-create/',
        'Update':'/sample-update/<str:pk>/',
        'Delete':'/sample-delete/<str:pk>/',
    }
    return JsonResponse(api_urls)

@csrf_exempt
def sampleList(request,id=0):
    if request.method == 'GET':
        samples = Sample.objects.all()
        sample_serializer = SampleSerializer(samples,many=True)

        return JsonResponse(sample_serializer.data, safe=False)

@csrf_exempt
def sampleCreate(request):
    if request.method == "POST":
        sample_data = JSONParser().parse(request)
        sample_serilizer = SampleSerializer(data=sample_data)
        if sample_serilizer.is_valid():
            sample_serilizer.save()
            return JsonResponse("Added Successfully",safe=False)

        return JsonResponse("Failed to Add",safe=False) 
        
@csrf_exempt
def sampleDetail(request,pk):
    if request.method == "GET":
        sample_data = Sample.objects.get(sampleId=pk)
        sample_serializer = SampleSerializer(sample_data,many=False)

        return JsonResponse(sample_serializer.data)

@csrf_exempt
def sampleUpdate(request,pk):
    if request.method == "PUT":
        sample_data = JSONParser().parse(request)
        sample = Sample.objects.get(sampleId=sample_data['sampleId'])
        sample_serilizer = SampleSerializer(sample,data=sample_data)
        if sample_serilizer.is_valid():
            sample_serilizer.save()
            return JsonResponse("Updated Successfully",safe=False)

        return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def sampleDelete(request,pk):
    if request.method == "DELETE":
        sample_data = Sample.objects.get(sampleId=pk)
        sample_data.delete()

    return Response("Item Successfuly deleted")

@csrf_exempt
def customerFirstOrLast(request):
    if request.method == "GET":
        customer = Customer.objects.first()
        customer_serializer = CustomerSerializer(customer,many=False)

        return JsonResponse(customer_serializer.data, safe=False)

@csrf_exempt
def customerByName(request,name):
    if request.method == "GET":
        customer_data = Customer.objects.get(name=name)
        customer_serializer = CustomerSerializer(customer_data, many=False)

        return JsonResponse(customer_serializer.data)

@csrf_exempt
def firstCustomerOrders(request):
     if request.method == "GET":
         first_customer = Customer.objects.first()
         orders = first_customer.order_set.all()
         order_serializer = OrderSerializer(orders, many=True)

         return JsonResponse(order_serializer.data, safe=False)

@csrf_exempt
def customerNameOfFirstOrder(request):
    if request.method == "GET":
        first_order = Order.objects.first()
        customer_name = first_order.customer.name

        return JsonResponse(customer_name, safe=False)

@csrf_exempt
def orderByCategory(request):
    if request.method == "GET":
        products = Product.objects.filter(category="Out Door")
        product_serializer = ProductSerializer(products, many=True)

        return JsonResponse(product_serializer.data, safe=False)

# Sorting
# leastToGratest = Product.objects.all()_order_by('id')
# greatestToLeast = Product.objects.all()_order_by('-id')

@csrf_exempt
def productByTags(request):
    if request.method == "GET":
        product = Product.objects.filter(tags__name="Sport")
        prodcut_serializer = ProductSerializer(product, many=True)

        return JsonResponse(prodcut_serializer.data, safe=False)

@csrf_exempt
def todalCountForEachProduct(request):

    allOrders = {}

    if request.method == "GET":
        first_customer = Customer.objects.first()
        for order in first_customer.order_set.all():
            if order.product.name in allOrders:
                allOrders[order.product.name] += 1
            else:
                allOrders[order.product.name] = 1

    return JsonResponse(allOrders, safe=False)            

