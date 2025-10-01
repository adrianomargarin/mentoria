from model_bakery import baker
from django.db.utils import IntegrityError
from django.test import TestCase
from mentoria.blog.models.post import Post


class PostModelsTest(TestCase):

    def setUp(self):
        self.category = baker.make('blog.Category')
        self.post = Post(category=self.category, title='Post Title', slug='slug', text='my text')
        self.post.save()

    def test_str(self):
        """Teste __str__ do models Post da app BLOG"""
        self.assertEqual(str(self.post), 'Post Title')
    
    def test_create_with_duplicate_slug(self):
        """Teste criação Post com mesmo slug"""
        with self.assertRaisesMessage(IntegrityError, 'DETAIL:  Key (slug)=(slug) already exists'):
            post = Post(category=self.category, title='Post Title', slug='slug', text='my text')
            post.save()
