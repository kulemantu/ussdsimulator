from django.conf.urls import url
from .views import UssdSimulator
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
urlpatterns = [
    url(r'^$', UssdSimulator.as_view(), name='ussd_simulator'),
]