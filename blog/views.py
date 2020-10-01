from django.views.generic import ListView

from blog.models import Article


class ArticlesView(ListView):
    model = Article
    queryset = Article.objects.filter(is_published=True)
    template_name = 'articles/overview.html'
