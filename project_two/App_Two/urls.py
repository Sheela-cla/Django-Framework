from django.urls import path
from App_Two import views

urlpatterns = [
    path('',views.index, name='index'),
]