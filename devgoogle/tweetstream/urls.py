from django.conf.urls import patterns, url

from tweetstream import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)