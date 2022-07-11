from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ParentCategory)
admin.site.register(ChildCategory)
admin.site.register(SubCategory)
admin.site.register(ProductImages)
admin.site.register(ProductDescriptions)

admin.site.register(Product)
admin.site.register(ProductModel)
admin.site.register(ProductType)
admin.site.register(CheckOut)
admin.site.register(CheckoutProducts)
