from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your models here.

class Session(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True, null=True)
    duration = models.DurationField()
    when = models.DateTimeField(auto_now=False, null=True)
    notes = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return 'session ' + str(self.id)