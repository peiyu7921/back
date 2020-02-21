# from rest_framework.decorators import throttle_classes
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserModelSerializers
# Create your views here.
# from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework import mixins
# import  rest_framework.status
# from rest_framework.throttling import AnonRateThrottle
class UserView(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializers
    # def update(self, request, *args, **kwargs):
    #     print(request.user)
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)

# @throttle_classes([AnonRateThrottle])

class createUser(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        ret = {'code': 201, 'msg': '注册成功'}
        data = request.data
        try:
            User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            try:
                user = User.objects.create_user(nick_name=data['nick_name'], email=data['email'],
                                                password=data['password'], avatar=request.FILES['avatar'])
                if user is not None:
                    user.save()
                    return Response(ret, status=ret['code'])
            except ValidationError as e:
                ret = {'code': 406, 'msg': e}
                return Response(ret, status=406)
        ret = {'code': 406, 'msg': 'email重复'}
        return Response(ret, status=ret['code'])

# permission_classes = (IsAuthenticated)
# def get(self, request, pk):
#     return self.retrieve(request)
#     # user = self.get_object()
#     # userSerializer = self.get_serializer(instance=user)
#     # return Response(userSerializer.data)
#
# def put(self, request, pk):
#     return self.update(request)
#     # instance = self.get_object()
#     # data = request.data
#     # serializer = self.get_serializer(instance=instance, data=data)
#     # serializer.is_valid(raise_exception=True)
#     # serializer.save()
#     # return Response(serializer.data)
#
# def delete(self, request, pk):
#     return self.destroy(request)


# class MulUserGenericView(ListAPIView, CreateAPIView):
#     queryset = queryset
#     serializer_class = UserModelSerializers
#
#     # # def get(self, request):
#     # #     user = self.get_queryset()
#     # #     userSerializer = self.get_serializer(instance=user, many=True)
#     # #     return Response(userSerializer.data)
#     # def get(self, request):
#     #     return self.list(request)
#     #
#     # def post(self, request):
#     #     return self.create(request)
#     # # serializer = self.get_serializer(data=request.data)
#     # # serializer.is_valid(raise_exception=True)
#     # # serializer.save()
#     # # return Response(serializer.data)
def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登录之后返回token和user信息
    """
    return {
        'token': token,
        'user': UserModelSerializers(user, context={'request': request}).data
    }