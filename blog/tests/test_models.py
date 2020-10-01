from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Article, Tag

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


class TagModelTest(TestCase):

    def test_can_be_created(self):
        Tag.objects.create(
            name='test tag'
        )

        tag = Tag.objects.first()
        uuid4_regexp = r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}$'

        self.assertRegexpMatches(tag.id, uuid4_regexp)
        self.assertEqual(tag.name, 'test tag')
