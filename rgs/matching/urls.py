from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.RGSUserViewSet, base_name='users')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]