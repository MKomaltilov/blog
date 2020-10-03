from django.utils.timezone import now
from uuid import uuid4

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField(to='Tag', related_name='articles', blank=True)
    publish_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
