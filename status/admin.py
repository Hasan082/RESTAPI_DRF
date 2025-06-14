from django.contrib import admin
from .models import Status
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Status models.
    """
    list_display = ('user', 'text', 'created_at', 'is_active', 'is_private')
    search_fields = ('user__username', 'text')
    list_filter = ('is_active', 'is_private', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Status, StatusAdmin)