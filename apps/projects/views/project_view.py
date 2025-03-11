from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.projects.models import Project
from django.utils import timezone

from apps.projects.serializers.project_serializer import AllProjectsSerializer


class ProjectView(APIView):

    def get_objects(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        data = Project.objects.all()
        if date_from:
            date_from = timezone.make_aware(datetime.strptime(date_from, '%Y-%m-%d'))
            data = data.filter(created_at__gte=date_from)
        if date_to:
            date_to = timezone.make_aware(datetime.strptime(date_to, '%Y-%m-%d'))
            data = data.filter(created_at__lte=date_to)
        return data

    def get(self, request):
        projects = self.get_objects(request)
        if not projects.exists():
            return Response({'error': 'No projects found'}, status=status.HTTP_204_NO_CONTENT)
        serializer = AllProjectsSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AllProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
