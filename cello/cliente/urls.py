from django.conf.urls import url
from cliente.views import *

urlpatterns = [
    url(r'^inserir/$', Cliente.as_view(), name='cliente_inserir'),
    url(r'^editar/$', Cliente.as_view(), name='cliente_editar'),
    url(r'^deletar/$', Cliente.as_view(), name='cliente_deletar'),
    url(r'^$', Cliente.as_view(), name='cliente'),
]
