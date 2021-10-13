from django.db import models

class Appointments(models.Model):
    first_name = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=10000)
    email = models.CharField(max_length=10000)
    phone = models.CharField(max_length=10000)
    request = models.TextField(blank=True)
    sent_date = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name_plural = 'appointments'
        ordering = ['-sent_date']


class Services(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=500)
    days_of_activities = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title

    @property
    def imagelink(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name_plural = 'services'
        # ordering = ['-id'] # it works

    
class Personnel(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=500)
    honor = models.CharField(max_length=300, blank=True, null=True)
    job_title = models.CharField(max_length=500)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'personnels'

    @property
    def personnelImage(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url