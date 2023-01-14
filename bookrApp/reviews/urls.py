from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_view, name="welcome_view"),
    path('book-search/', views.book_search, name='book_search'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]
