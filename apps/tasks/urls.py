from django.urls import path
from apps.tasks.views.tag_view import TagView

urlpatterns = [
    path('tags/', TagView.as_view(), name='tags'),
]
