from django.contrib import admin
from users.models import profile

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as baseAdmin

@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'phone', 'bio')
    search_fields = ('user__email', 'phone',
                     'user__first_name', 'user__last_name')
    list_filter = ('created', 'modified')

class profileInline(admin.StackedInline):
    model=profile
    can_delete=False
    verbose_name_plural='profiles'

class userAdmin(baseAdmin):
    inlines=(profileInline,)

admin.site.unregister(User)
admin.site.register(User,userAdmin)