from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']
        unique_together = ('name', 'description')



    def __str__(self):
        return self.name