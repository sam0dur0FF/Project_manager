from django.db import models


class ProjectFile(models.Model):
    name = models.CharField(max_length=120, verbose_name="Название файла")
    file = models.FileField(upload_to="documents/", verbose_name="Файл")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания файла")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Файл проекта"
        verbose_name_plural = "Файлы проекта"

    def __str__(self):
        return self.name

