from django.urls import path
from rest_framework import routers
from .api import ConcViewSet
from . import views

router = routers.DefaultRouter()
router.register('conc', ConcViewSet, 'conc')
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('report/', views.report, name='report')
]

urlpatterns += router.urls
