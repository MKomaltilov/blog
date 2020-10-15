from django.urls import path
from blog.views import ArticlesView

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles'),
]
