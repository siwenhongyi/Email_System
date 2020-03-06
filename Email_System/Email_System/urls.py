"""
Definition of urls for Email_System.
"""

from datetime import datetime
from django.urls import path
from django.contrib.staticfiles.views import serve
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('favicon.ico/', serve, {'path': 'app/ico/logo.png'}),
    #path('favicon.ico/',RedirectView.as_view(url='static/app/ico/favicon.ico')), 

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('login/',views.login,name='login'),
    path('logon/',views.logon,name = 'logon'),
    path('logout/',views.logout, name='logout'),
    path('admin/', admin.site.urls),

    path('home_page/',views.home_page,name = 'home_page'),
    path('writeletter/',views.writeletter,name = 'writeletter'),
    path('sendletter/',views.sendletter,name = 'sendletter'),
    path('inbox/',views.inbox,name = 'inbox'),
    path('sendbox/',views.sendbox,name = 'sendbox'),
    path('mail/',views.mail,name = 'mail'),
    path('addressbook/',views.addressbook,name = 'addressbook'),
    path('settings/',views.settings,name = 'settings'),

    path('download/',views.download_attachment,name = 'download'),
    path('mailmenu/',views.mailmenu,name = 'mailmenu'),
]