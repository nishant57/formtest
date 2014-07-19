from django.conf.urls import patterns, url
from addnum import views

urlpatterns = patterns('',
	url(r'^$', views.addnum, name='addnum'),
)
