
from django.conf.urls import patterns, url
from genviewbks.views import PublisherList, PublisherDetail

urlpatterns = patterns('',
	url(r'^publishers/$', PublisherList.as_view()),
	url(r'^publisher/(?P<name>[-_\w]+)/$', PublisherDetail.as_view()),
)
