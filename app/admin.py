from django.contrib import admin
from .models import Appointments, Services, Personnel


admin.site.register(Appointments)
admin.site.register(Services)
admin.site.register(Personnel)