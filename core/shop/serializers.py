from abc import ABC
from statistics import mode

from .models import *
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
import json
from django.core.serializers import serialize





class ChildCategorySerializer(ModelSerializer):
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = ChildCategory
        fields = ['title', 'subcategory']

    def get_subcategory(self, obj):
        return json.loads(serialize(format='json', queryset=obj.subcategory_set.all()))


class ParentCategorySerializer(ModelSerializer):
    # childs = ChildCategorySerializer(read_only=True)
    # subcategories = serializers.SerializerMethodField()

    class Meta:
        model = ParentCategory
        fields = '__all__'

    # def get_childs(self, obj):
    #     return json.loads(serialize(format='json', queryset=obj.childcategory_set.all()))

    # def get_subcategories(self, obj):
    #     for i in obj.childcategory_set.all():
    #         return json.loads(serialize(format='json', queryset=i.subcategory_set.all()))


class SubCategorySerializer(ModelSerializer):
    child = ChildCategorySerializer()

    class Meta:
        model = SubCategory
        fields = ['title', 'child']


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductDescriptionsSerializer(ModelSerializer):
    class Meta:
        model = ProductDescriptions
        fields = '__all__'


class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    
class ProductCategory2Serializer(ModelSerializer):
    class Meta:
        model = ChildCategory
        fields = '__all__'


class ProductCategory1Serializer(ModelSerializer):
    class Meta:
        model = ParentCategory
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category1 = ProductCategory1Serializer()
    category2 = ProductCategory2Serializer()
    category3 = ProductCategorySerializer()
    images = ProductImageSerializer(read_only=True, many=True)
    description = ProductDescriptionsSerializer(read_only=True, many=True)
    type = ProductTypeSerializer()
    model = ProductModelSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class FilterSerializer(Serializer):
    category = serializers.ListField()
    min_price = serializers.FloatField()
    max_price = serializers.FloatField()


class CheckoutSerializer(Serializer):
    checkout_products = serializers.ListField()
    


class CheckoutProductSerializer(ModelSerializer):
    class Meta:
        model = CheckoutProducts
        fields = '__all__'

    
class OrderedProductsSerializer(ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = CheckOut
        fields = '__all__'