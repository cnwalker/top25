from readers.views import IndexView
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^readers/', include('readers.urls', namespace='readers')),
    
)
