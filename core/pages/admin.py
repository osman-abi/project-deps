from django.contrib import admin
from .models import *
from .about.models import *
# Register your models here.

# admin.site.register(AskQuestion)

@admin.register(AskQuestion)
class AskQuestionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'question'
    ]

@admin.register(WriteDirector)
class WriteDirectorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'question'
    ]

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'position'
    ]


admin.site.register(About)
admin.site.register(Slide)