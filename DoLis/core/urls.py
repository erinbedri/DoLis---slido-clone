from django.urls import path

from DoLis.core import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('my-events/', views.own_events_list, name='own events list'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('event/<int:pk>/', views.event_details, name='event details'),
    path('event/<int:pk>/edit/', views.event_edit, name='event edit'),
    path('event/<int:pk>/delete/', views.event_delete, name='event delete'),
    path('event/create/', views.event_create, name='event create'),
    path('question/<int:pk>/delete', views.question_delete, name='question delete')
]