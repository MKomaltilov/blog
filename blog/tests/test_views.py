from django.test import TestCase


class ArticlesOverviewPageTest(TestCase):

    def test_articles_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'articles/overview.html')
