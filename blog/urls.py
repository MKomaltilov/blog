from django.urls import path
from blog.views import ArticlesView, article_view, tag_view

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles'),
    path('articles/<int:article_id>', article_view, name='article_view'),
    path('tags/<uuid:tag_id>', tag_view, name='tag_view')
]
