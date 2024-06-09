from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage1, name="HomePage1"),
    path('signIn', views.signIn, name="signIn"),
    path('salon2', views.salon2, name="salon2"),
    path('Contactus', views.Contactus, name="Contactus"),
    path('BeautyExperts', views.BeautyExperts, name="BeautyExperts"),
    path('BookingPage', views.BookingPage, name="BookingPage"),
    path('Aboutas2', views.Aboutas2, name="Aboutas2"),
    path('reserve', views.reserve, name='reserve'),  
]
