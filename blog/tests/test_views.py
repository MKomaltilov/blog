from django.test import TestCase
from django.utils.timezone import now
from blog.models import Article, Tag


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

    def test_tags_for_article_exists_on_page(self):
        article = Article.objects.create(
            title='first',
            content='Test article content',
            is_published=True
        )
        tag_one = Tag.objects.create(name='tag one')
        tag_two = Tag.objects.create(name='tag two')
        tag_three = Tag.objects.create(name='tag three')

        article.tags.add(tag_one)
        article.tags.add(tag_three)

        response = self.client.get('/')

        self.assertContains(response, 'first')
        self.assertContains(response, 'tag one')
        self.assertContains(response, 'tag three')

        self.assertNotContains(response, 'tag two')

    def test_shows_publish_date_in_right_format(self):
        datetime_now = now()
        Article.objects.create(
            title='first',
            content='Test article content',
            is_published=True,
            publish_date=datetime_now
        )

        response = self.client.get('/')
        self.assertContains(response, datetime_now.strftime("%d.%m.%Y %H:%M"))

    def test_shows_content_not_more_than_300_symbols(self):
        content = 'a' * 500
        Article.objects.create(
            title='first',
            content=content,
            is_published=True
        )

        response = self.client.get('/')

        max_content = 'a' * 300
        self.assertContains(response, max_content)
        self.assertNotContains(response, content)

