from django.urls import path
from . import views

urlpatterns = [
    path('filter_concerts/', views.filter_concerts, name='filter_concerts'),
    path('', views.concert_list, name='concert_list'),
    path('create/', views.concert_create, name='concert_create'),
    path('<int:id>/edit/', views.concert_edit, name='concert_edit'),
    path('<int:id>/delete/', views.concert_delete, name='concert_delete'),
    path('<int:concert_id>/book/', views.book_ticket, name='book_ticket'),
    path('filter_concerts/', views.filter_concerts, name='filter_concerts'),
    path('book_ticket_form/<int:concert_id>/', views.book_ticket, name='book_ticket_form'),
    path('<int:concert_id>/book/', views.book_ticket, name='book_ticket'),
path('success/', views.success_page, name='success_page'),

]






