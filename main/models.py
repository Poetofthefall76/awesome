from django.db import models
from django.utils import timezone


class Question(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"

    def create(self):
        self.created_date = timezone.now()
        self.save()


class Image(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="", blank=True)
    file = models.FileField(upload_to="", blank=True)

    def __str__(self):
        return f"{self.title}"
