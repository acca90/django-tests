from django.views.generic import TemplateView
from django.apps import apps


class Principal(TemplateView):
    template_name = 'principal/index.html'
    apps = apps.get_models()

    def get_context_data(self, **kwargs):
        context = super(Principal, self).get_context_data(**kwargs)

        context['modulos'] = {}

        return context
