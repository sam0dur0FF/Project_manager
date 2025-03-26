from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.projects.models import ProjectFile
from apps.projects.serializers.project_file_serializers import AllProjectFilesSerializer, CreateProjectFileSerializer, \
    ProjectFileDetailSerializer


class ProjectFileListAPIView(APIView):

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return AllProjectFilesSerializer(*args, **kwargs)
        elif self.request.method == 'POST':
            return CreateProjectFileSerializer(*args, **kwargs)

    def get_objects(self, project_name=None):
        if not project_name:
            return ProjectFile.objects.all()
        return ProjectFile.objects.filter(project__name=project_name)

    def get(self, request):
        project_name = request.query_params.get("name")
        project_files = self.get_objects(project_name)
        if not project_files.exists():
            return Response({'error': 'No files found'}, status=status.HTTP_204_NO_CONTENT)
        serializer = self.get_serializer(project_files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectFileDetailView(RetrieveDestroyAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileDetailSerializer
