from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('api.userMana.urls')),
                       url(r'', include('api.authMana.urls')),
                       url(r'', include('api.customerMana.urls')),

                       )
