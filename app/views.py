
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.http import HttpResponse, request
from django.conf import settings
from django.contrib import messages
from .models import Appointments, Services, Personnel
from django.views.generic import ListView
import datetime
# import django.template import 
from django.template.loader import get_template, render_to_string


class Home(TemplateView):
    template_name = 'app/index.html'
    def get_context_data(self, *args, **kwargs): 
        context =  super().get_context_data(*args,**kwargs)
        services = Services.objects.all()
        personnel = Personnel.objects.all()
        context.update({
            'services':services,
            'personnel': personnel
        })
        return context

    def post(self, request):
        name= request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        email = EmailMessage(
            subject= f'{name} from umezuruike hosp. ltd.',
            body=message,
            from_email= email,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        messages.info(self.request, "Email sent successfully", extra_tags="success")
        return redirect('home')


class Appointment(TemplateView):
    template_name = 'app/appointment.html'

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message_request = request.POST.get('request')

        appointment = Appointments.objects.create(
            first_name = fname,
            last_name=lname, 
            email=email,
            phone=number,
            request=message_request
        )
        

        appointment.save()
        messages.info(self.request, f"thanks {fname} for booking an appointment, we will get back to you ", extra_tags="success")
        return redirect('appointment')
    
class ManageAppointment(ListView):
    template_name = 'app/manage-appointments.html'
    model = Appointments
    context_object_name = 'appointments'
    login_required  = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get('date')
        appointment_id = request.POST.get('appointment.id')
        appointment = Appointments.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        

        data = {
            'fname': appointment.first_name,
            'date': date,
            'request_body': appointment.request
        }
        message = get_template('app/email.html').render(data)
        email = EmailMessage(
            'About Your Appointment',
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email]
        )
        email.content_subtype='html'
        email.send()
        # incase the message fails
        # first of all, send the email before saving the appointment as true
        appointment.save()
 
        messages.info(self.request,f"You accepted the appointment of {appointment.first_name}", extra_tags="success")
        return redirect('manage-appointments')

    # pulling out the data from the database 
    def get_context_data(self, *args, **kwargs): 
        context =  super().get_context_data(*args,**kwargs)
        appointments = Appointments.objects.all()
        context.update({
            'title':'Manage Appointments'
        })
        return context

class History(TemplateView):
    template_name = 'app/history.html'