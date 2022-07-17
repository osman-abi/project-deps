import json
from django.core.serializers import serialize
from django.http import JsonResponse

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter

from .serializers import CheckoutSerializer, ParentCategorySerializer, ProductImageSerializer, ProductSerializer, FilterSerializer, OrderedProductsSerializer
from .models import CheckOut, CheckoutProducts, ChildCategory, ParentCategory, Product, ProductImages
from .utils import related_products


# Create your views here.

class CategoryAPIView(ListAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer
    permission_classes = [AllowAny]

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes

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

class FeaturedProductAPIView(ListAPIView):
    queryset = Product.objects.filter(is_featured=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class BestsellerProductAPIView(ListAPIView):
    queryset = Product.objects.filter(is_bestseller=True)
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
            categories = serializer.validated_data.get('category3')
            min_price = serializer.validated_data.get('min_price', '')
            max_price = serializer.validated_data.get('max_price', '')
            kwargs['category__id__in'] = categories
            kwargs['price__gt'] = min_price
            kwargs['price__lt'] = max_price
            products = Product.objects.filter(**kwargs)
            products_ = json.loads(serialize('json',products))
            return Response(products_, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilterProductByParentCategory(APIView):

    def post(self,request):
        kwargs = dict()
        serializer = FilterSerializer(data=request.data)
        if serializer.is_valid():
            categories = serializer.validated_data.get('category1')
            min_price = serializer.validated_data.get('min_price', '')
            max_price = serializer.validated_data.get('max_price', '')
            kwargs['category__id__in'] = categories
            kwargs['price__gt'] = min_price
            kwargs['price__lt'] = max_price
            products = Product.objects.filter(**kwargs)
            products_ = json.loads(serialize('json',products))
            return Response(products_, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilterProductByChildCategory(APIView):

    def post(self,request):
        kwargs = dict()
        serializer = FilterSerializer(data=request.data)
        if serializer.is_valid():
            categories = serializer.validated_data.get('category2')
            min_price = serializer.validated_data.get('min_price', '')
            max_price = serializer.validated_data.get('max_price', '')
            kwargs['category__id__in'] = categories
            kwargs['price__gt'] = min_price
            kwargs['price__lt'] = max_price
            products = Product.objects.filter(**kwargs)
            products_ = json.loads(serialize('json',products))
            return Response(products_, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CheckOutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer_class = CheckoutSerializer(data=request.data)
        if serializer_class.is_valid():
            checkout_products_ = serializer_class.validated_data.get('checkout_products')
            check = CheckOut.objects.create(user=request.user)
            for i in checkout_products_:
                check_prod = CheckoutProducts.objects.create(
                    product_id = i.get('product_id'),
                    quantity = i.get('quantity'),
                )
                check.checkout_products.add(check_prod)
                check.save()
        #     serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ordered_products(request,pk):
    checkout = CheckOut.objects.filter(pk=pk).first()
    checkout_products = checkout.checkout_products.all()
    # print('print >>>', checkout_products)

    array = []
    json_ = dict()
    for i in checkout_products:
        product = Product.objects.filter(id=i.product_id)
        array.append(json.loads(serialize('json', product)))
        json_['quantity'] = i.quantity
        json_['data'] = array
    return JsonResponse(json_, safe=False)


class CheckoutProductsAPIView(ListAPIView):
    queryset = CheckoutProducts.objects.all()
    serializer_class = OrderedProductsSerializer
    permission_classes = [IsAuthenticated]


category_api = CategoryAPIView.as_view()
product_api = ProductAPIView.as_view()
search_api = SearchProductAPIView.as_view()
filter_api = FilterProductAPIView.as_view()
filter_by_parent_api = FilterProductByParentCategory.as_view()
filter_by_child_api = FilterProductByChildCategory.as_view()
product_detail = ProductDetailAPIView.as_view()
related_product_api = RelatedProductAPIView.as_view()
checkout = CheckOutAPIView.as_view()
featured_products = FeaturedProductAPIView.as_view()
best_products = BestsellerProductAPIView.as_view()
checkout_product = CheckoutProductsAPIView.as_view()
