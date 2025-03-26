from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone
from apps.projects.models import Project
from apps.projects.serializers.project_serializer import ProjectShortInfoSerializer
from apps.tasks.choices.priority import PriorityEnum
from apps.tasks.models import Task, Tag


class AllTasksSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    assignee = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Task
        fields = [
            'title',
            'status',
            'priority',
            'project',
            'assignee',
            'deadline',
        ]


class CreateUpdateTaskSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Project.objects.all(),
    )

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'priority',
            'project',
            'tag',
            'assignee',
            'deadline',
        ]

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Title must be at least 2 characters')
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Description must be at least 2 characters')
        return value

    def validate_priority(self, value):
        value = value.title()
        if value not in PriorityEnum.choices_values():
            raise serializers.ValidationError('Priority must be one of: {}'.format(PriorityEnum.choices_values()))
        return value

    def validate_project(self, value):
        result = Project.objects.filter(name=value)
        if not result:
            raise serializers.ValidationError('Project does not exist')
        return value

    def validate_tag(self, value):
        all_unique_tags_name = Tag.objects.filter(name__in=value)

        if not all_unique_tags_name:
            raise serializers.ValidationError('Tags not found')
        return value

    def validate_deadline(self, value):
        if not isinstance(value, datetime):
            value = datetime.fromisoformat(value)
        if value < timezone.now():
            raise serializers.ValidationError('Deadline must be in the future')
        return value

    def create(self, validated_data):
        tags = validated_data.pop('tag', [])
        instance = Task.objects.create(**validated_data)
        instance.tag.set(tags)
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop('tag', [])
        instance.tag.set(tags)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance


class TaskDetailSerializer(serializers.ModelSerializer):
    project = ProjectShortInfoSerializer()

    class Meta:
        model = Task
        exclude = ['updated_at', 'deleted_at']
