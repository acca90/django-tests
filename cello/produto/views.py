from django.shortcuts import render
from django.template import RequestContext
from django.views import View


class Produto(View):
    template_name = 'produto/index.html'

    def get(self, request):
        context = RequestContext(request)

        return render(request, self.template_name)

