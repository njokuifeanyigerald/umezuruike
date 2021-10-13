from django.urls import path
from .views import Home, Appointment, ManageAppointment, History
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Home.as_view() , name='home' ),
    path('appointment/', Appointment.as_view(), name='appointment'),
    path('manage-appointment/', login_required(ManageAppointment.as_view()), name='manage-appointments'),
    path('history/', History.as_view(), name='history'),
]
