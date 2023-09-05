from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import RegisterForm
from .models import Session

from django.urls import reverse_lazy
from django.utils.dateparse import parse_duration
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

class Chronometer(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            sessions = request.user.session_set.all()
        else: sessions = 0
        return render(request, 'index.html', {'sessions':sessions})

    def post(self, request, *args, **kwargs):
        sess = Session(duration = parse_duration(request.POST.get('duration')), notes = request.POST.get('notes'), user = request.user)
        sess.save()
        return HttpResponseRedirect('')

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