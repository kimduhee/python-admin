from django.urls import path
from . import views

urlpatterns = [
    path('submain', views.adminuserSubmain, name='adminuserSubmain'),
    path('list', views.adminuserList, name='adminuserList'),
]