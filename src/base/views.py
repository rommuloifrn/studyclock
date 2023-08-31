from django.shortcuts import render
from django.views import View
from .models import Session

from django.utils.dateparse import parse_duration
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

class Chronometer(View):
    def get(self, request, *args, **kwargs):
        sessions = Session.objects.all()
        return render(request, 'index.html', {'sessions':sessions})

    def post(self, request, *args, **kwargs):
        # request.POST.get('duration')
        sess = Session(duration = parse_duration(request.POST.get('duration')), notes = request.POST.get('notes'))
        sess.save()
        

        return HttpResponseRedirect('')
