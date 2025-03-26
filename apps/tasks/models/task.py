from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from apps.projects.models import Project
from apps.tasks.choices.priority import PriorityEnum
from apps.tasks.choices.statuses import StatusEnum
from apps.tasks.models import Tag
from apps.tasks.utils.set_end_of_month import calculate_end_of_month


class Task(models.Model):
    title = models.CharField(validators=[MinLengthValidator(10)], max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=11, choices=StatusEnum.choices(), default=StatusEnum.NEW)
    priority = models.CharField(max_length=10, choices=PriorityEnum.choices(), default=PriorityEnum.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=calculate_end_of_month)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.OneToOneField(User, on_delete=models.CASCADE, related_name='task', null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='tasks')

    def __str__(self):
        return f'{self.priority}: {self.title} -> {self.status}'

    class Meta:
        ordering = ['-deadline', 'assignee']
        unique_together = (('project', 'title'),)

