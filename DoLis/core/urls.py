from django.urls import path

from DoLis.core import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('event/<int:pk>/', views.event_details, name='event details'),
    path('event/create/', views.event_create, name='event create')
]