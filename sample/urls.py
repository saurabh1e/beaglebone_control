__author__ = 'saurabh'
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

from sample import views


urlpatterns = patterns('sample.views',
        url(r'^$', views.main_page, name='main'),
        url(r'^rooms/', views.rooms, name='rooms'),
        url(r'^appliances/$', views.appliances, name='app'),
        url(r'^wireless/', views.wireless, name='wireless'),
        url(r'^appliances/(?P<t_id>[-\w.]+)', views.toggle, name='toggle'),

)