from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.Chronometer.as_view(), name='chrono'),
    path('login', views.Login.as_view(), name='login'),
]