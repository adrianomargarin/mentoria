from django.db.utils import IntegrityError
from django.test import TestCase
from mentoria.blog.models.tag import Tag


class PostModelsTest(TestCase):

    def setUp(self):
        self.post = Tag(name='tag')
        self.post.save()

    def test_str(self):
        """Teste __str__ do models Tag da app BLOG"""
        self.assertEqual(str(self.post), 'tag')
    
    def test_create_with_duplicate_slug(self):
        """Teste criação Tag com mesmo nome"""
        with self.assertRaisesMessage(IntegrityError, 'DETAIL:  Key (name)=(tag) already exists.'):
            post = Tag(name='tag')
            post.save()
