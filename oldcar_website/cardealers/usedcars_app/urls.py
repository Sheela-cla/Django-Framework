from django.urls import path
from usedcars_app import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('search/', views.car_search, name='car_search'),
]