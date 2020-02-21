# from django.conf.urls import url
from .views import SiteNodeViewSet, spider
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    # path('user', UserView.as_view({'get': 'list'})),
    # re_path(r'user/(?P<pk>\d+)', UserView.as_view({'get': 'retrieve', 'post': 'create','put': 'update',
    #                                                'delete': 'destroy'}))
]
router = DefaultRouter()

router.register('site_node', SiteNodeViewSet)

urlpatterns += router.urls