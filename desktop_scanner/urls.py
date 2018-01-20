"""desktop_scanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from scanner.views import home
from account.views import login_view, collect_or_deposit_view
from scanner.views import  start_collect, start_deposit, start_confirmation_modal

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view, name='login'),
    url(r'^collect_or_deposit', collect_or_deposit_view, name='collect_or_deposit'),
    url(r'^collect', start_collect, name='start_collect'),
    url(r'^deposit', start_deposit, name='start_deposit'),
    url(r'^confirmation_modal', start_confirmation_modal, name='confirmation_modal')

]
