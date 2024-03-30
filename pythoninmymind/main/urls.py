from django.urls import path
from .views import MainPage, article_detail, search, AllArticles
from .sitemaps import ArticleSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'articles': ArticleSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('articles/<str:slug>', article_detail, name='article'),
    path('search/', search, name='search'),
    path('all-articles/', AllArticles.as_view(), name='all_articles'),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    )
]