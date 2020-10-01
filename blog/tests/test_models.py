from django.test import TestCase

from blog.models import Article, Tag


class ArticleModelTest(TestCase):

    def test_can_be_created_with_default_params(self):
        Article.objects.create(
            title='Test article',
            content='Test article content'
        )

        article = Article.objects.first()

        self.assertEqual(article.title, 'Test article')
        self.assertEqual(article.content, 'Test article content')
        self.assertFalse(article.is_published)

    def test_can_have_tags(self):
        tag_one = Tag.objects.create(name='tag one')
        tag_two = Tag.objects.create(name='tag two')
        tag_three = Tag.objects.create(name='tag three')

        new_article = Article.objects.create(
            title='Test article',
            content='Test article content'
        )
        new_article.tags.add(tag_one)
        new_article.tags.add(tag_three)

        created_article = Article.objects.first()
        tags_in_article = created_article.tags.all()

        self.assertIn(tag_one, tags_in_article)
        self.assertIn(tag_three, tags_in_article)

        self.assertNotIn(tag_two, tags_in_article)

    def test_str_shows_title(self):
        Article.objects.create(
            title='Test article',
            content='Test article content'
        )

        article = Article.objects.first()

        self.assertEqual(str(article), 'Test article')


class TagModelTest(TestCase):

    def test_can_be_created(self):
        Tag.objects.create(
            name='test tag'
        )

        tag = Tag.objects.first()
        uuid4_regexp = r'[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'

        self.assertRegexpMatches(str(tag.id), uuid4_regexp)
        self.assertEqual(tag.name, 'test tag')
