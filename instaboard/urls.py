from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('account', views.account, name='account'),
  path('follow', views.follow, name='follow'),
  path('<slug:slug>', views.detail, name='detail'),
]