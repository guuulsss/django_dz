from django.contrib import admin
from .models import BugReport, FeatureRequest

# Администратор для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'priority', 'created_at', 'updated_at')
    list_filter = ('priority', 'project', 'task')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'priority', 'project', 'task')
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    actions = ['change_bug_status']

    def change_bug_status(self, request, queryset):
        queryset.update(priority='2')  # Пример изменения статуса

    change_bug_status.short_description = 'Изменить статус бага'

# Администратор для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('priority', 'status', 'project', 'task')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'priority', 'status', 'project', 'task')
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
