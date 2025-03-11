from rest_framework import serializers

from apps.projects.models import Project


class AllProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = [
            'files',
        ]
