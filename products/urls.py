from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='products_index'),
    path('new', views.new, name='products_new')
]