from django.views.generic import ListView

from blog.models import Article


class ArticlesView(ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'articles/overview.html'
