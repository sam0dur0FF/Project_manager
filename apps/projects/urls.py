from django.urls import path
from apps.projects.views.project_file_views import ProjectFileListAPIView
from apps.projects.views.project_view import ProjectView, ProjectDetailAPIView

urlpatterns = [
    path('', ProjectView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailAPIView.as_view(), name='project_details'),
    path('files/', ProjectFileListAPIView.as_view(), name='project_files'),

]
