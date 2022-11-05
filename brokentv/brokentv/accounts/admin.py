from django.contrib import admin

from brokentv.accounts.models import Profile, BrokenTvUser


@admin.register(BrokenTvUser)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
