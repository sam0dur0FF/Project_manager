from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from apps.tasks.models import Task
from apps.tasks.serializers.tasks_serializers import AllTasksSerializer, CreateTaskSerializer


class TasksListPaginator(PageNumberPagination):
    max_page_size = 30
    page_size = 5


class AllTasksListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    pagination_class = TasksListPaginator

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllTasksSerializer
        elif self.request.method == 'POST':
            return CreateTaskSerializer

    def filter_queryset(self, queryset):
        project_name = self.request.query_params.get('project')
        employee_name = self.request.query_params.get('employee')
        if project_name:
            queryset = queryset.filter(project__name=project_name)
        if employee_name:
            queryset = queryset.filter(assignee__name=employee_name)
        return queryset
