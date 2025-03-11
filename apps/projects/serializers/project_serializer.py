from rest_framework import serializers

from apps.projects.models import Project


class AllProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = [
            'files',
        ]

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = 'name', 'description', 'created_at', 'count_of_files'

