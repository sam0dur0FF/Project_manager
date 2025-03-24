from rest_framework import serializers

from apps.projects.models import ProjectFile, Project
from apps.projects.utils.upload_file_helpers import EXTENSTIONS, check_extension, check_file_size, save_file, \
    create_file_path


class AllProjectFilesSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        many=True,
    )
    class Meta:
        model = ProjectFile
        fields = '__all__'


class CreateProjectFileSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        write_only=True
    )

    class Meta:
        model = ProjectFile
        fields = 'name', 'file', 'project_id'

    def validate_name(self, value: str) -> str:
        if not value.isascii():
            raise serializers.ValidationError(
                "Please, provide a valid file name."
            )
        return value

    def validate_file(self, value):
        if not check_file_size(value):
            raise serializers.ValidationError(
                "File size is too large (2 MB as maximum)."
            )

        if not check_extension(value.name):
            raise serializers.ValidationError(
                f"Valid file extensions: {EXTENSTIONS}"
            )

        return value

    def create(self, validated_data):
        file = validated_data['file']  # файловый дескриптор django
        file_path = create_file_path(file_name=file.name)
        save_file(file_path=file_path, file_data=file)
        validated_data['file'] = file_path

        project = validated_data.pop('project_id')
        project_file = ProjectFile.objects.create(**validated_data)
        project_file.projects.add(project)

        return project_file
