from django.db import models


class About(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name='başlıq')
    context = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Haqqımızda'


class OurTeam(models.Model):
    profile = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='ad')
    surname = models.CharField(max_length=200, blank=True, null=True, verbose_name='soyad')
    position = models.CharField(max_length=200, blank=True, null=True, verbose_name='vəzifə')

    class Meta:
        verbose_name_plural = 'Komandamızın üzvləri'