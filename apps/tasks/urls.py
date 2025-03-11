from django.urls import path
from apps.tasks.views.tag_view import TagView, TagDetailApiView

urlpatterns = [
    path('tags/', TagView.as_view(), name='tags'),
    path('tags/<int:pk>', TagDetailApiView.as_view(), name='tag'),

]
