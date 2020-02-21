import django_filters
import requests
# from threading import Timer
import datetime
import time, json

import asyncio

# from asgiref.sync import sync_to_async
from django_filters import FilterSet
# from rest_framework.settings import api_settings
#
# from .serializers import SiteNodeModelSerializers
# def creatTimer():
#     t = Timer(5, spider())
#     t.start()
#     return None
from rest_framework.viewsets import mixins, GenericViewSet
from .models import SiteNode
from .serializers import SiteNodeModelSerializers
# Create your views here.

class SiteNodeFilter(FilterSet):
    siteName = django_filters.CharFilter(field_name='siteName', lookup_expr="icontains")  # icontains 包含,忽略大小写
    dateTimeRange = django_filters.DateFromToRangeFilter(field_name='dateTime')
    class Meta:
        model = SiteNode  # 关联的模型
        fields = ['siteName']


class SiteNodeViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = SiteNode.objects.all()
    serializer_class = SiteNodeModelSerializers
    filter_fields = ['siteName']
    filterset_class = SiteNodeFilter


def spider():
    while(True):
        r = requests.post('http://123.127.175.45:8082/ajax/GwtWaterHandler.ashx', data={'Method':'SelectRealData'})
        data = json.loads(r.text)
        for site in data:
            for key in site:
                try:
                    site[key] = float(site[key])
                except ValueError:
                    continue
        serializer = SiteNodeModelSerializers(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(datetime.datetime.now())
        time.sleep(60)
        # creatTimer()
    # return r.text


# import threading
#
# spiderThread = threading.Thread(target=spider, name='spider')
# spiderThread.start()