from django.urls import path

from apps.projects.views.project_view import ProjectView, ProjectDetailAPIView
from apps.tasks.views.tag_view import TagView, TagDetailApiView

urlpatterns = [
    path('', ProjectView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailAPIView.as_view(), name='project_details'),

]
