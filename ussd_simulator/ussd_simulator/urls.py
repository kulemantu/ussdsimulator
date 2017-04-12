from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
    url(r'^simulator/', include('simulator.urls')),
    url(r'^admin/', admin.site.urls),
]