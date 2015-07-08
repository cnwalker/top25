import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'views.IndexView', name = 'index'),
    url(r'^(?P<reader_id>\d+)/$', views.AnalysisView, name = 'analysis'),
    url(r'^archive/$', views.ArchiveView, name = 'archive')
)
