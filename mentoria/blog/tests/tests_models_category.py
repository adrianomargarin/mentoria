from django.test import TestCase
from django.db.utils import IntegrityError
from mentoria.blog.models.category import Category


class CategoryModelsTest(TestCase):

    def setUp(self):
        self.category = Category(name='Category Name', slug='slug')
        self.category.save()

    def test_str(self):
        """Teste __str__ do models Category da app BLOG"""
        self.assertEqual(str(self.category), 'Category Name')
    
    def test_create_with_duplicate_slug(self):
        """Teste criação Category com mesmo slug"""
        with self.assertRaisesMessage(IntegrityError, 'DETAIL:  Key (slug)=(slug) already exists'):
            category = Category(name='name', slug='slug')
            category.save()
