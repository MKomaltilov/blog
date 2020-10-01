from django.test import TestCase

from blog.models import Article


class ArticlesOverviewPageTest(TestCase):

    def test_articles_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'articles/overview.html')

    def test_published_articles_appears_on_page(self):
        Article.objects.create(
            title='first',
            content='Test article content',
            is_published=True
        )

        Article.objects.create(
            title='second',
            content='Test article content'
        )

        Article.objects.create(
            title='third',
            content='Test article content',
            is_published=True
        )

        response = self.client.get('/')

        self.assertContains(response, 'first')
        self.assertContains(response, 'third')

        self.assertNotContains(response, 'second')
