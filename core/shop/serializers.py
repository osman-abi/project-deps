from abc import ABC

from .models import *
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
import json
from django.core.serializers import serialize


class ParentCategorySerializer(ModelSerializer):
    childs = serializers.SerializerMethodField()
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = ParentCategory
        fields = ['title', 'childs', 'subcategories']

    def get_childs(self, obj):
        return json.loads(serialize(format='json', queryset=obj.childcategory_set.all()))

    def get_subcategories(self, obj):
        for i in obj.childcategory_set.all():
            return json.loads(serialize(format='json', queryset=i.subcategory_set.all()))


class ChildCategorySerializer(ModelSerializer):
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = ChildCategory
        fields = ['title', 'subcategory']

    def get_subcategory(self, obj):
        return json.loads(serialize(format='json', queryset=obj.subcategory_set.all()))


class SubCategorySerializer(ModelSerializer):
    child = ChildCategorySerializer()

    class Meta:
        model = SubCategory
        fields = ['title', 'child']


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


class ProductSerializer(ModelSerializer):
    category = ProductCategorySerializer()
    type = ProductTypeSerializer()
    model = ProductModelSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class FilterSerializer(Serializer):
    category = serializers.ListField()
    min_price = serializers.FloatField()
    max_price = serializers.FloatField()
