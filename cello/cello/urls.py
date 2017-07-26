from django.conf.urls import url
from django.contrib import admin
from principal.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Principal.as_view(), name='index')
]
