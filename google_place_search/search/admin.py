from django.contrib import admin

from .models import Trial


@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    pass
