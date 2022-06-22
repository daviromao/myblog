from django.db import models


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('withdrawn', 'Withdrawn'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    summary = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
    