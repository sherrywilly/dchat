from django.urls import path
from chat import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:c_name>/<str:room_name>/', views.room, name='room'),
    path('s/<str:c_name>/<str:room_name>/', views.room2, name='room2'),
    path('<str:c_name>/', views.hitter, name='hit'),
    path('<str:c_name>/room/close/', views.close_chat, name='close'),
]
