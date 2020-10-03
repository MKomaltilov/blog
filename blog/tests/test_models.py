from django.test import TestCase
from django.db import IntegrityError, transaction

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

    def test_have_a_publish_date_and_sorted_by_this_field(self):
        Article.objects.create(
            title='Test article 1',
            content='Test article content'
        )
        Article.objects.create(
            title='Test article 2',
            content='Test article content'
        )
        Article.objects.create(
            title='Test article 3',
            content='Test article content'
        )
        Article.objects.create(
            title='Test article 4',
            content='Test article content'
        )

        articles = Article.objects.all()

        self.assertEqual(articles[0].title, 'Test article 4')
        self.assertIsNotNone(articles[0].publish_date)
        self.assertEqual(articles[1].title, 'Test article 3')
        self.assertIsNotNone(articles[1].publish_date)
        self.assertEqual(articles[2].title, 'Test article 2')
        self.assertIsNotNone(articles[2].publish_date)
        self.assertEqual(articles[3].title, 'Test article 1')
        self.assertIsNotNone(articles[3].publish_date)


class TagModelTest(TestCase):

    def test_can_be_created(self):
        Tag.objects.create(
            name='test tag'
        )

        tag = Tag.objects.first()
        uuid4_regexp = r'[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'

        self.assertRegexpMatches(str(tag.id), uuid4_regexp)
        self.assertEqual(tag.name, 'test tag')

    def test_str_shows_name(self):
        Tag.objects.create(
            name='test tag'
        )

        tag = Tag.objects.first()

        self.assertEqual(str(tag), 'test tag')

    def test_name_is_unique_field(self):
        Tag.objects.create(
            name='test tag'
        )

        try:
            with transaction.atomic():
                Tag.objects.create(
                    name='test tag'
                )
        except IntegrityError:
            pass

        tags_amount = Tag.objects.count()
        self.assertEqual(tags_amount, 1)
