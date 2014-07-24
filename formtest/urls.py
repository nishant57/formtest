from django.conf.urls import patterns, include, url
from bookdb import views
from django.views.generic import TemplateView
# from bookdb.views import UserDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'formtest.views.home', name='home'),
    # url(r'^formtest/', include('formtest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#	url(r'^users/(?P<user>[\w]+)/$', UserDetail.as_view()),
	url(r'^home/', views.index , name = "index"),
	url(r'^accounts/profile/', TemplateView.as_view(template_name='bookdb/profile.html')),
	url(r'^users/', TemplateView.as_view(template_name='bookdb/profile.html')),
	url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^books/', include('genviewbks.urls')),
	url(r'^addnum/', include('addnum.urls')),
)

#   <a href="{% url 'index' %}">{% trans "Home" %}</a> |"}"'}"
