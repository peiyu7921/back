from .models import SiteNode
from rest_framework import serializers


class SiteNodeModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SiteNode
        fields = "__all__"