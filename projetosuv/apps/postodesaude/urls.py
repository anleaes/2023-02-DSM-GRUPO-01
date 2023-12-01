from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'postodesaude'

router = routers.DefaultRouter()
router.register('', views.PostoDeSaudeViewSet, basename='postodesaude')

urlpatterns = [
    path('', include(router.urls) )
]