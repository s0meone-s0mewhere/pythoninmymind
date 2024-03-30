from django.shortcuts import render, get_object_or_404
from . models import *
from .forms import *
from django.views.generic.list import ListView
from django.contrib.postgres.search import SearchVector

# Create your views here.

class MainPage(ListView):
    model = Article
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().filter(is_published=True)[:3]
        return context
    
def article_detail(request, slug):
    context = {}
    context['article'] = get_object_or_404(Article, slug=slug)
    context['recommended_articles'] = Article.objects.all().filter(is_published=True).exclude(slug=slug)[:4]
    return render(request, 'main/article.html', context=context)

def search(request):
    form = SearchForm()
    query = None
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Article.objects.annotate(search=SearchVector('title', 'content'), ).filter(search=query, is_published=True)

            return render(request, 'main/search.html', context={'form': form, 'query': query, 'results': results})

    return render(request, 'main/search.html', context={'form': form})

class AllArticles(ListView):
    paginate_by = 24
    model = Article
    template_name = 'main/all_articles.html'
    context_object_name = 'articles'
    
    def get_queryset(self):
        context = Article.objects.all().filter(is_published=True)
        return context