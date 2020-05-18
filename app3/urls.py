from django.conf.urls import url

import app3.views as views

urlpatterns = [
    url(r'^blocknotify/$', views.blocknotify, name='cc-blocknotify'),
    url(r'^walletnotify/$', views.walletnotify, name='cc-walletnotify'),
]
