from django.shortcuts import render
from django.template import loader, RequestContext
from django.views import View


class Principal(View):
    template_name = 'principal/index.html'

    def get(self, request):
        context = RequestContext(request)

        return render(request, self.template_name)
