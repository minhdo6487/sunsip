from django.contrib import admin
# import reversion

from core.user.models import UserProfile, GroupChat


# # class UserProfileAdmin(reversion.VersionAdmin):
# class UserProfileAdmin(reversion.admin.VersionAdmin):
#     search_fields = ['user__username']
#     list_display = ('user', 'display_name', 'handicap_us',)
#
# # class GroupchatAdmin(reversion.VersionAdmin):
# class GroupchatAdmin(reversion.admin.VersionAdmin):
# 	pass
#
# admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(GroupChat, GroupchatAdmin)