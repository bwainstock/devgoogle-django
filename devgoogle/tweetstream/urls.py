from django.conf.urls import patterns, url

from tweetstream import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<tag>\w+)/$', views.tag, name='tag'),
	url(r'^latest/$', views.latest, name='latest'),
)