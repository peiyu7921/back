from django.conf.urls import url
from .views import UserView, createUser
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url('^user/login/', obtain_jwt_token),# POST email=email&password=password
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^user/logup/', createUser.as_view()),
    # path('user', UserView.as_view({'get': 'list'})),
    # re_path(r'user/(?P<pk>\d+)', UserView.as_view({'get': 'retrieve', 'post': 'create','put': 'update',
    #                                                'delete': 'destroy'}))
]
router = DefaultRouter()

router.register('user', UserView)

urlpatterns += router.urls