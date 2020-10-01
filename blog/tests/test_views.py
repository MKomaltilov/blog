from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Article

User = get_user_model()


class ArticlesOverviewPageTest(TestCase):

    def test_articles_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'articles/overview.html')

    def test_published_articles_appears_on_page(self):
        user = User.objects.create(
            username='user',
            password='123'
        )
        Article.objects.create(
            title='first',
            content='Test article content',
            author=user,
            is_published=True
        )

        Article.objects.create(
            title='second',
            content='Test article content',
            author=user
        )

        Article.objects.create(
            title='second',
            content='Test article content',
            author=user,
            is_published=True
        )

        response = self.client.get('/')

        self.assertContains(response, 'first')
        self.assertContains(response, 'third')

        self.assertNotContains(response, 'second')
