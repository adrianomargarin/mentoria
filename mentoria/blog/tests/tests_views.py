from datetime import datetime
from model_bakery import baker
from django.test import TestCase
from django.urls import reverse_lazy, reverse
from mentoria.blog.models import Post


class PostListViewTestCase(TestCase):
    def setUp(self):
        self.posts = baker.make('blog.Post', published_at=datetime.now(), _quantity=10)
        self.response = self.client.get(reverse_lazy('blog:index'))

    def test_total_count(self):
        "Verifica o total de posts criados"
        self.assertEqual(Post.objects.count(), 10)

    def test_paginated_by(self):
        "Verifica o total de posts paginados"
        self.assertEqual(self.response.context['posts'].count(), 5)

    def test_is_paginated(self):
        "Verifica se paginou posts"
        self.assertTrue(self.response.context['is_paginated'])


class PostDetailViewTestCase(TestCase):
    def setUp(self):
        self.post = baker.make('blog.Post', published_at=datetime.now())
        self.response = self.client.get(reverse_lazy('blog:detail', args=[self.post.category.slug, self.post.slug]))

    def test_content(self):
        "verifica se conteúdo está visivel na página"
        expected_content = [self.post.title, self.post.subtitle, self.post.text]

        with self.subTest():
            for value in expected_content:
                self.assertIn(value, self.response.content.decode('utf-8'))


class AboutViewTestCase(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse_lazy('blog:about'))

    def test_content(self):
        expected_content = [
            'Olá, eu sou o Adriano',
            'Python e Django',
            'Mentoria Django',
            'Vamos construir algo incrível juntos?'
        ]

        with self.subTest():
            for value in expected_content:
                self.assertIn(value, self.response.content.decode('utf-8'))