from django.conf.urls import url
from produto.views import *

urlpatterns = [
    url(r'^inserir/$', Produto.as_view(), name='produto_inserir'),
    url(r'^editar/$', Produto.as_view(), name='produto_editar'),
    url(r'^deletar/$', Produto.as_view(), name='produto_deletar'),
    url(r'^$', Produto.as_view(), name='cliente'),
]
