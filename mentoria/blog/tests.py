from django.test import TestCase
from mentoria.blog.models import Category


class CategoryModelsTest(TestCase):

    def setUp(self):
        self.category = Category(name='Category Name', slug='slug')
        self.category.save()

    def test_str(self):
        """Teste STR do models Category da app BLOG"""
        self.assertEqual(str(self.category), 'Category Name')
