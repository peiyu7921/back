from django.db.models import Q

from .models import User
from rest_framework import serializers


class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nick_name', 'email', 'avatar']