from django.contrib import admin

# Register your models here.
from campapp.models import *

@admin.register(Camper)
class CamperAdmin(admin.ModelAdmin):
    pass

@admin.register(CampTeam)
class CampTeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass

@admin.register(TeamScheduledActivity)
class TeamSchActivityAdmin(admin.ModelAdmin):
    pass

@admin.register(CamperActivity)
class CamperActivityAdmin(admin.ModelAdmin):
    pass