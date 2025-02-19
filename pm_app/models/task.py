from django.contrib.auth.models import User
from django.db import models
from enum import Enum
from pm_app.models import Project, Tag




class StatusEnum(Enum):
    NEW ='New'
    IN_PROGRES = 'In Progress'
    COMPLETED = 'Completed'
    CLOSED = 'Closed'
    PENDING = 'Pending'
    BLOCKED = 'Blocked'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class PriorityEnum(Enum):
    LOW ='Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]



class Task(models.Model):
    STATUS_CHOICES = StatusEnum.choices()
    PRIORITY_CHOICES = PriorityEnum.choices()

    title = models.CharField(min_length=10, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.priority}: {self.title} -> {self.status}'

    class Meta:
        ordering = ['-deadline', 'assignee']
        unique_together = (('project', 'title'),)
