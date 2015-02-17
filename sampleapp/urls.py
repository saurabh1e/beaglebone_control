from django.conf.urls import patterns, include, url
from django.contrib import admin
import sample
from django.conf.urls.static import  static
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('sample.urls', namespace='sample')),
) 


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
