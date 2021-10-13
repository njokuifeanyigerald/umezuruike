from .models import Appointments

def get_notification(request):
    count = Appointments.objects.filter(accepted=False).count()
    data = {
        'count':count
    }
    return data

# will be added to the settings.py file 
# in the context processor 

# there is 3 ways of doing this..
# 1 is this way
# 2 is through the models.py file
#  3 is directly in the views.py file