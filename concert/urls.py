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
path('booking_successful/<str:concert_name>/', views.booking_successful, name='booking_successful'),

path('submit_booking/', views.submit_booking, name='submit_booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
path('contact_us/', views.contact_us, name='contact_us'),
    path('<int:concert_id>/book/', views.book_ticket, name='book_ticket'),
path('pay/', views.pay, name='pay'),
    path('confirm_mpesa/', views.confirm_mpesa, name='confirm_mpesa'),
    path('process_payment/', views.process_payment, name='process_payment'),
 path('submit_refund/', views.submit_refund, name='submit_refund'),
]








