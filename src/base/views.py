from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.dateparse import parse_duration
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.views import View
from django.views.generic import CreateView
#from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RegisterForm
from .models import Session
from django.contrib.auth.models import User
from datetime import timedelta



def index(request):
    return render(request, 'index.html')

class Chronometer(View):
    def get(self, request, *args, **kwargs):
        # isso aqui está meio gambiarra!
        if request.user.is_authenticated:
            sessions = request.user.session_set.all().order_by('-saved')
        else: sessions = 0
        return render(request, 'index.html', {'sessions':sessions})

    def post(self, request, *args, **kwargs):
        sess = Session(duration = parse_duration(request.POST.get('duration')), notes = request.POST.get('notes'), user = request.user)
        sess.save()
        return HttpResponseRedirect('')

class DeleteSession(View):
    def post(self, request, *args, **kwargs):
        sess = get_object_or_404(Session, pk=kwargs['pk'])
        if sess.user == request.user and request.user.is_authenticated:
            sess.delete()
        return HttpResponseRedirect('/')

class ViewOwnProfile(View):
    def get(self, request):
        user = request.user
        hours = timedelta()
        for sess in user.session_set.all():
            hours = hours + sess.duration
        return render(request, 'profile.html', {'user':user, 'hours': hours})

class ManuallyCreateSession(View):
    def post(self, request, *args, **kwargs):
        duration = request.POST.get('hours') + ":" + request.POST.get('minutes') + ":" + request.POST.get('seconds')
        time = request.POST.get('hour')+"-"+request.POST.get('minute')+"-"+request.POST.get('second')
        date = request.POST.get('date')

        sess = Session(
            duration = parse_duration(duration), 
            notes = request.POST.get('notes'),
            user = request.user,
            saved=datetime.strptime(date + " " + time, '%Y-%m-%d %H-%M-%S')
        )

        sess.save() 
        return HttpResponseRedirect('/')

class Login(LoginView):
    next_page = '/'
    redirect_authenticated_user = True
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('chrono')

class Logout(LogoutView):
    next_page = reverse_lazy('chrono')

class SignUp(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('chrono')

