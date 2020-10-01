from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Article

User = get_user_model()


class ArticleModelTest(TestCase):

    def test_can_be_created_with_default_params(self):
        user = User.objects.create(
            username='user',
            password='123'
        )
        Article.objects.create(
            title='Test article',
            content='Test article content',
            author=user
        )

        article = Article.objects.first()

        self.assertEqual(article.title, 'Test article')
        self.assertEqual(article.content, 'Test article content')
        self.assertEqual(article.author, user)
        self.assertFalse(article.is_published)
