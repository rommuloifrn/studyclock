from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import datetime

# Create your models here.

class StudyClockTools():
    def user_today_hours(user):
        sessions = user.session_set.all().order_by('-saved')
        hours = datetime.timedelta()
        # MUITO ineficiente
        for s in sessions:
            if s.saved.date() == datetime.datetime.now().date():
                hours = hours + s.duration
        return hours

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True, null=True)
    duration = models.DurationField()
    saved = models.DateTimeField() # https://docs.djangoproject.com/en/4.1/topics/i18n/timezones/
    last_edit = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.user) + ' -  ' + str(self.saved)