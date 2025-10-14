from datetime import datetime
from model_bakery import baker
from django.contrib import admin
from django.test import TestCase, RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage
from mentoria.blog.models.post import Post
from mentoria.blog.admin.post import PostAdmin


class PostAdminTestCase(TestCase):
    def setUp(self):
        baker.make(Post, _quantity=5)
        baker.make(Post, published_at=datetime.now(), _quantity=10)

        self.user = baker.make('auth.User')
        self.factory = RequestFactory()

        self.post_admin = PostAdmin(Post, admin.site)

    def _add_messages_middleware(self, request):
        setattr(request, 'session', {})
        storage = FallbackStorage(request)
        setattr(request, '_messages', storage)
        
        return storage

    def test_action_publish(self):
        request = self.factory.get("/")
        request.user = self.user
        storage = self._add_messages_middleware(request)
    
        self.post_admin.action_publish(request, Post.objects.all())
        msgs = list(storage)

        self.assertEqual(len(msgs), 1)
        self.assertEqual(msgs[0].message, '5 POSTs publicados.')