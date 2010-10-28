from django.conf.urls.defaults import *

urlpatterns = patterns('picoblog.views',
    url(r'^$', 'main', name='main'),
    url(r'^follow/(?P<id>\d+)$', 'follow', name='follow'),
)
