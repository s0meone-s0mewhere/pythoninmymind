from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = MarkdownxField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('article', args=[self.slug])

    class Meta:
        ordering = ['-date_created', ]