from django.urls import path, include


urlpatterns = [
    path('tags/', include('apps.tags.urls')),
]
