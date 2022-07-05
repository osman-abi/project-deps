import json
from django.core.serializers import serialize
from django.http import JsonResponse

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter

from .serializers import CheckoutSerializer, ParentCategorySerializer, ProductImageSerializer, ProductSerializer, FilterSerializer, OrderedProductsSerializer
from .models import CheckOut, ChildCategory, ParentCategory, Product, ProductImages
from .utils import related_products


# Create your views here.

class CategoryAPIView(ListAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer
    permission_classes = [AllowAny]

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

@swagger_auto_schema(method='get')
@api_view(['GET'])
def child_categories(request,pk):
    parent = ParentCategory.objects.get(pk=pk)
    childs = parent.childcategory_set.all()
    data = json.loads(serialize(format='json', queryset=childs))
    return JsonResponse(data, safe=False)


@swagger_auto_schema(method='get')
@api_view(['GET'])
def sub_categories(request,pk):
    parent = ChildCategory.objects.get(pk=pk)
    childs = parent.subcategory_set.all()
    data = json.loads(serialize(format='json', queryset=childs))
    return JsonResponse(data, safe=False)



class ImagesAPIView(ListAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [AllowAny]


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class SearchProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("title",)


class RelatedProductAPIView(APIView):
    def get(self, request, pk):
        return related_products(pk)



class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class FilterProductAPIView(APIView):

    def post(self, request):
        kwargs = dict()
        serializer = FilterSerializer(data=request.data)
        if serializer.is_valid():
            categories = serializer.validated_data.get('category')
            min_price = serializer.validated_data.get('min_price', '')
            max_price = serializer.validated_data.get('max_price', '')
            kwargs['category__id__in'] = categories
            products = Product.objects.filter(**kwargs)
            products_ = json.loads(serialize('json',products))
            return Response(products_, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckOutAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer_class = CheckoutSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderedProductsAPIView(ListAPIView):
    queryset = CheckOut.objects.all()
    serializer_class = OrderedProductsSerializer
    permission_classes = [AllowAny]


category_api = CategoryAPIView.as_view()
product_api = ProductAPIView.as_view()
search_api = SearchProductAPIView.as_view()
filter_api = FilterProductAPIView.as_view()
product_detail = ProductDetailAPIView.as_view()
related_product_api = RelatedProductAPIView.as_view()
checkout = CheckOutAPIView.as_view()
ordered_products = OrderedProductsAPIView.as_view()
