from django.contrib import admin
from .models import *
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

class ArticleAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title',)

admin.site.register(Article, ArticleAdmin)