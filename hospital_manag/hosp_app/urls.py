from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment', views.TakeAppointment, name='appointment'),
    path('appointmentBooked', views.appointmentBooked, name='appointmentbook'),
    path('change', views.change, name='delete'),
    path('deleted/<int:id>', views.deleted, name='deleted'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update,name='update')
]