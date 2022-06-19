from .models import SubCategory, Product
from rest_framework.response import Response
from django.core.serializers import serialize
import json


def related_products(pk):
    product = Product.objects.get(pk=pk)
    sub_category = SubCategory.objects.filter(id=product.category.id).first()
    related_prods = sub_category.product_set.all()
    subcategory = json.loads(serialize('json', related_prods))
    return Response(subcategory)
