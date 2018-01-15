from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
urlpatterns =  patterns('',
                       url(r'^api/v1_0/', include('api.urls')),
                       # url(r'^api/v2/', include('v2.api.urls')),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
