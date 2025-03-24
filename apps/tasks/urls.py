from django.urls import path
from apps.tasks.views.tag_view import TagView, TagDetailApiView
from apps.tasks.views.task_view import AllTasksListAPIView

urlpatterns = [
    path('tags/', TagView.as_view(), name='tags'),
    path('tags/<int:pk>', TagDetailApiView.as_view(), name='tag'),
    path('tasks/', AllTasksListAPIView.as_view(), name='tasks'),

]
