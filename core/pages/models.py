from ctypes import addressof
from django.db import models


# Create your models here.
class RequestPrice(models.Model):
    category = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name='ad')
    email = models.EmailField(blank=True, null=True, verbose_name='poçt ünvanı')
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='tel')
    message = models.TextField(blank=True, null=True, verbose_name='mesaj')


class AskQuestion(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name='ad')
    email = models.EmailField(blank=True, null=True, verbose_name='poçt ünvanı')
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='tel')
    question = models.TextField(blank=True, null=True, verbose_name='soruşulan sual')

    class Meta:
        verbose_name_plural = 'Soruşulan suallar'


class WriteDirector(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name='ad')
    company_name = models.CharField(max_length=250, blank=True, null=True, verbose_name='müəssisə adı')
    email = models.EmailField(blank=True, null=True, verbose_name='poçt ünvanı')
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='tel')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='şəhər')
    question = models.TextField(blank=True, null=True, verbose_name='context')

    class Meta:
        verbose_name_plural = 'Direktora yazılanlar'


class Slide(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True, verbose_name='başlıq')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='slide/')
    mobile_image = models.ImageField(upload_to='mobile/')
    text_string = models.TextField()

    def __str__(self):
        return self.title


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Info(models.Model):
    address       = models.CharField(max_length=300, blank=True, null=True)
    email_address = models.CharField(max_length=300, blank=True, null=True)
    number1       = models.CharField(max_length=300, blank=True, null=True) 
    number2       = models.CharField(max_length=300, blank=True, null=True) 
    number3       = models.CharField(max_length=300, blank=True, null=True) 
    openTimes     = models.CharField(max_length=300, blank=True, null=True)
    coordinates   = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.address