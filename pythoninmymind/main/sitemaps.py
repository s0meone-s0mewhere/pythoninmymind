"""
Django sitemap framework docs: https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/
Also used https://pocoz.gitbooks.io/django-v-primerah/content/rasshirenie-prilozheniya-blog/dobavlenie-sitemap.html
"""
from django.contrib.sitemaps import Sitemap
from .models import Article
from django.urls import reverse


class ArticleSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return Article.objects.all().filter(is_published=True)
    

class StaticViewSitemap(Sitemap):
    changefreq = 'always'
    protocol = 'https'
    priority = 1.0
    
    def items(self):
        items = [
            'main',
            'all_articles',
        ]
        return items
    
    def location(self, item):
        return reverse(item)