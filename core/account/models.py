from django.db import models
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.



class MyUserManager(BaseUserManager):
    def create_user(self, email,name,password=None, phone_number=None, surname=None, address=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            address=address,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            name=name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(
        verbose_name='istifadəçi adı',
        max_length=300,
        blank=True,
        null=True
    )
    surname = models.CharField(
        verbose_name='istifadəçi soyadı',
        max_length=300,
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name='istifadəçi ünvanı',
        max_length=300,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='poçt ünvanı',
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(
        verbose_name='tel',
        max_length=20,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
