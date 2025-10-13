from model_bakery import baker
from django.db.utils import IntegrityError
from django.test import TestCase
from datetime import datetime
from mentoria.blog.models.post import Post


class PostModelsTest(TestCase):

    def setUp(self):
        self.published_at = datetime.now()
        self.user = baker.make('auth.User')
        self.category = baker.make('blog.Category')

        self.post = Post(
            category=self.category,
            title='Post Title',
            slug='slug',
            text='my text',
            created_by=self.user,
            published_by=self.user,
            published_at=self.published_at,
        )
        self.post.save()

    def test_str(self):
        """Teste __str__ do models Post da app BLOG"""
        self.assertEqual(str(self.post), 'Post Title')

    def test_field_values(self):
        expected_values = {
            'category': self.category,
            'title': 'Post Title',
            'slug': 'slug',
            'text': 'my text',
            'created_by': self.user,
            'published_by': self.user,
            'published_at': self.published_at,
        }

        for key, value in expected_values.items():
            with self.subTest():
                self.assertEqual(getattr(self.post, key), value)

    def test_create_with_duplicate_slug(self):
        """Teste criação Post com mesmo slug"""
        with self.assertRaisesMessage(IntegrityError, 'DETAIL:  Key (slug)=(slug) already exists'):
            post = Post(
                category=self.category,
                title='Post Title',
                slug='slug',
                text='my text',
                created_by=self.user,
                published_by=self.user,
                published_at=self.published_at,
            )
            post.save()
