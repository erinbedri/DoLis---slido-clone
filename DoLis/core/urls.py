from django.urls import path

from DoLis.core import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]