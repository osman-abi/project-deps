from pyexpat import model
from django.db import models
from account.models import User
# Create your models here.

class ParentCategory(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='başlıq')

    def __str__(self):
        return self.title


class ChildCategory(models.Model):
    parent = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='başlıq')

    def __str__(self):
        return f"{self.parent} => {self.title}"


class SubCategory(models.Model):
    child = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='başlıq')
    is_populated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.child} => {self.title}"




class ProductImages(models.Model):
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.image.url

class ProductType(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductModel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description


class ProductDescriptions(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description


class Product(models.Model):
    category1 = models.ForeignKey("ParentCategory", on_delete=models.CASCADE, blank=True, null=True)
    category2 = models.ForeignKey("ChildCategory", on_delete=models.CASCADE, blank=True, null=True)
    category3 = models.ForeignKey("SubCategory", on_delete=models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField(ProductImages)
    manifacturer = models.CharField(max_length=200, blank=True, null=True, verbose_name='istehsalçı')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='başlıq')
    weight = models.FloatField(blank=True, null=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    model = models.ManyToManyField(ProductModel)
    description = models.ManyToManyField(ProductDescriptions)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    code = models.CharField(max_length=9, blank=True, null=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.id

    def save(self):
        import string
        import random
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits,k=9))
        self.code = ran
        return super(Product, self).save()


class CheckoutProducts(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)


class CheckOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_products = models.ManyToManyField(CheckoutProducts, blank=True)


    

    def __str__(self):
        return str(self.id)

