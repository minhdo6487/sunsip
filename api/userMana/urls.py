from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from django.contrib import admin

from api.userMana.views import UserViewSet, ProfileView

from utils.rest import routers as addedrouters
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


get_urls = patterns('', url(r'^user/get_group/$', 'api.userMana.views.get_group'))
update_user_version = patterns('', url(r'^user/version', 'api.userMana.views.update_user_version'))
urlpatterns = get_urls + update_user_version + patterns('',url(r'', include(router.urls)))

addedrouter = addedrouters.GetAndUpdateRouter()
addedrouter.register(r'profile', ProfileView, base_name='profile')

urlpatterns += format_suffix_patterns(patterns('',
                                               url(r'', include(addedrouter.urls))))
