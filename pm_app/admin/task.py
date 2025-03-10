from django.contrib import admin
from apps.projects.models.project import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = "title",
    list_display = ("title", "project", "status", "priority", "created_at", "deadline")
    list_filter = ("status", "project", "priority", "created_at", "deadline")