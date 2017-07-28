from django.shortcuts import render
from django.template import RequestContext
from django.views import View


class Cliente(View):
    template_name = 'cliente/index.html'

    def get(self, request):
        context = RequestContext(request)

        return render(request, self.template_name)

