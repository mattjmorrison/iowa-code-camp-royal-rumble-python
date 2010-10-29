from django.conf.urls.defaults import *

urlpatterns = patterns('picoblog.views',
    url(r'^$', 'main', name='main'),
    url(r'^post_message/$', 'post_message', name='post_message'),
    url(r'^follow/$', 'follow', name='follow'),
)
