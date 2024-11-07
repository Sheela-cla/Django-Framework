from django.urls import path
from book_app import views

app_name = 'book_app'

urlpatterns = [
    path('categories/',views.Category_list, name ='categories'),
    path('',views.BookViews,name='bookviews'),
    path('bookdetails/<int:id>/', views.BookDetails, name='bookdetails'),
]