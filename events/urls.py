from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events_list, name='events_list'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/<int:event_id>/register/', views.register_event, name='register_event'),
    path('register/', views.register_user, name='register'),
]