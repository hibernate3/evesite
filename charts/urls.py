from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('chart_base/', views.chart_base, name='chart_base'),
]