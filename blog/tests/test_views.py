from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Article

User = get_user_model()


class ArticlesOverviewPageTest(TestCase):

    def test_articles_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'articles/overview.html')

    def test_articles_appears_on_page(self):
        user = User.objects.create(
            username='user',
            password='123'
        )
        new_article = Article.objects.create(
            title='Test article',
            content='Test article content',
            author=user
        )

        response = self.client.get('/')
        print(response)
        self.assertContains('Test article', response)
