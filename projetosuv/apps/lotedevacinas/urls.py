from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'lotedevacinas'

router = routers.DefaultRouter()
router.register('', views.LoteDeVacinasViewSet, basename='lotedevacinas')

urlpatterns = [
    path('', include(router.urls) )
]