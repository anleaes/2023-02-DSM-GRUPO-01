from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'vacinas'

router = routers.DefaultRouter()
router.register('',views.VacinaViewSet, basename='vacinas')

urlpatterns = [
    path('',include(router.urls))
]