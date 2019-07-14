from django.urls import *
from spider.views import *

app_name = 'spider'

urlpatterns = [
    path('', Crawler.as_view(), name='crawler_add'),
]
