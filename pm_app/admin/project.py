from django.contrib import admin
from apps.projects.models.project import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
