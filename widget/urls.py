from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^$', 'widget.views.list'),
  url(r'^(\w+)/$', 'widget.views.view', name='thingster'),
)
