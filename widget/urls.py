from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

  url(r'^(\w+)/$', 'widget.views.view', name='thingster'),
)
