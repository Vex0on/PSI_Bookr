from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('book-search/', views.book_search, name='book-search')
]
