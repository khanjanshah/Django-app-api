from django.urls import path, include
from rest_framework.routers import DefaultRouter

from model import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'model'

urlpatterns = [
    path('', include(router.urls))
]
