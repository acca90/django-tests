from django.conf.urls import url, include
from django.contrib import admin
from principal.views import *

urlpatterns = [
    url(r'^$', Principal.as_view(), name='index'),
    url(r'^cliente/', include('cliente.urls')),
    url(r'^produto/', include('produto.urls')),
    url(r'^admin/', admin.site.urls),
]
