from django.views.generic import ListView
from django.shortcuts import render

from blog.models import Article


class ArticlesView(ListView):
    model = Article
    queryset = Article.objects.filter(is_published=True)
    template_name = 'articles/overview.html'


def article_view(request, article_id):
    article = Article.objects.get(pk=article_id)

    return render(request, 'articles/article.html', {"article": article})
