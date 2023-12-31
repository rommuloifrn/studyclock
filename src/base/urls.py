from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.Chronometer.as_view(), name='chrono'),
    path('delete-session/<int:pk>', views.DeleteSession.as_view(), name='delsession'),
    path('profile', views.ViewOwnProfile.as_view(), name='profile'),
    path('manually-session', views.ManuallyCreateSession.as_view(), name='man'),

    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register', views.SignUp.as_view(), name='register'),
]