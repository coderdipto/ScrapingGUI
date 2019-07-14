import json

from django.http import JsonResponse
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from utils.helpers import scrape_data


class Crawler(View, TemplateResponseMixin):
    template_name = 'crawler_add.html'

    def get(self, request):
        return self.render_to_response(context={})

    def post(self, request):
        urls = request.POST.getlist('url', None)
        names = request.POST.getlist('name', [])
        values = request.POST.getlist('value', [])
        types = request.POST.getlist('type')
        data = []

        for url in urls:
            data.append(scrape_data(url, names, values, types))

        return JsonResponse(data, safe=False)
