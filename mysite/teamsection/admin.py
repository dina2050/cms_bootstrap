from django.contrib import admin
from .models import TeamMember
# Register your models here.
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember