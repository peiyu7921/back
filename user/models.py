from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class MyUserManager(BaseUserManager):
    def create_user(self, nick_name, email, password, avatar):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not nick_name:
            raise ValidationError('nick_name must have an nick_name')
        if not email:
            raise ValidationError('email must have an email address')
        else:
            try:
                print(validate_email(email))
                validate_email(email)
            except ValidationError as e:
                raise e
        if not password:
            raise ValidationError('password must have an email address')
        user = self.model(
            nick_name=nick_name,
            email=self.normalize_email(email),
            avatar=avatar
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nick_name, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            nick_name=nick_name,
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nick_name', 'password']
    nick_name = models.CharField(max_length=20, verbose_name='用户名')
    email = models.CharField(max_length=30, verbose_name='邮箱', unique=True)
    avatar =models.ImageField(upload_to='img', default='img/default.png')
    logup_time = models.DateTimeField(auto_now_add=True, editable=False)
    update_time = models.DateTimeField(auto_now_add=True)
    objects = MyUserManager()

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
