from django.conf.urls import patterns, include, url
from django.contrib import admin
import sample
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'sample/', include('sample.urls', namespace='sample')),
)
