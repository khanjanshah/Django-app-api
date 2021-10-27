from django.urls import path, include
from rest_framework.routers import DefaultRouter

from model import views


router = DefaultRouter()
router.register('data', views.DataIngestionViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'model'

urlpatterns = [
    path('', include(router.urls))
]
