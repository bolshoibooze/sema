from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from yawdadmin import admin_site
admin_site._registry.update(admin.site._registry)
from accounts.views import IndexRedirectView

#----------- TastyPie APIs-------------#
from tastypie.api import Api
v1_api = Api(api_name='v1')

from chat.api.resources import *
from therapists.api.resources import *
from payments.api.resources import *
from accounts.api.resources import *

"""
v1_api.register(ChatResource())
v1_api.register(TherapistsResource())
v1_api.register(PaymentsResource())
v1_api.register(UserResource())
"""


urlpatterns = patterns('',
    url(r'^$',IndexRedirectView.as_view()),
    
    url(r'^chat/',include('chat.urls')),
    url(r'^therapists/',include('therapists.urls')),
    url(r'^payments/',include('payments.urls')),
    url(r'^ua_detector/',include('ua_detector.urls')),
    url(r'^accounts/',include('accounts.urls')),
    
    
    
     url(r'^api/', include(v1_api.urls)),
    
    #admin stuff  
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^darknet/', include(admin.site.urls)),
    #url(r'^admin/', include(admin.site.urls)),
)
