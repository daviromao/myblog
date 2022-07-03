from django.db import models


class Base(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Tag(Base):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Post(Base):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('withdrawn', 'Withdrawn'),
    ]

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts', related_query_name='post', blank=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
    