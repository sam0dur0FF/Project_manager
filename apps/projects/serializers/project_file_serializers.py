from rest_framework import serializers

from apps.projects.models import ProjectFile
from apps.projects.utils.upload_file_helpers import EXTENSTIONS, check_extension, check_file_size, save_file


class AllProjectFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ('id', 'name', 'created_at', 'project')




class CreateProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ('name',)

    def validate_name(self, value):
        if not value.isascii():
            raise serializers.ValidationError(
                "Please, provide a valid file name."
            )
        if not check_extension(value):
            raise serializers.ValidationError(
                    f"Valid file extensions: {EXTENSTIONS}"
                )
        return value


    def create(self, validated_data):
        file_name = validated_data['name']
        raw_file=self.context.get("raw_file")
        if check_file_size(raw_file):
            save_file(file_name, raw_file)
            return super().create(validated_data)

        raise serializers.ValidationError("File size is too large.")






