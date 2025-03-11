from django.urls import path

from apps.projects.views.project_view import ProjectView
from apps.tasks.views.tag_view import TagView, TagDetailApiView

urlpatterns = [
    path('', ProjectView.as_view(), name='projects'),
    # path('tags/<int:pk>', TagDetailApiView.as_view(), name='tag'),

]
