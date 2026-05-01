from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data) 




@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    serilizer = ProductSerializer(product)
    related_serializer = ProductSerializer(related_products, many=True)

    return Response({
        'product': serilizer.data,
        'related_products': related_serializer.data
    })