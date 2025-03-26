from django.urls import path

from apps.tasks.serializers.tasks_serializers import CreateUpdateTaskSerializer
from apps.tasks.views.tag_view import TagView, TagDetailApiView
from apps.tasks.views.task_view import AllTasksListAPIView, TaskDetailAPIView

urlpatterns = [
    path('tags/', TagView.as_view(), name='tags'),
    path('tags/<int:pk>', TagDetailApiView.as_view(), name='tag'),
    path('', AllTasksListAPIView.as_view(), name='tasks'),
    path('<int:pk>/', TaskDetailAPIView.as_view(), name='task_detail'),

]

