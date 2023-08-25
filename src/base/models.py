from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True, null=True)
    duration = models.DurationField()
    when = models.DateTimeField(auto_now=False, auto_now_add=False)
    notes = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return 'session ' + str(self.id)