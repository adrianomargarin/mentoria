from django.urls import path
from mentoria.blog.views import PostListView, PostDetailView, AboutView

app_name = 'blog'

urlpatterns = [
    path('<slug:category_slug>/<slug:post_slug>/', PostDetailView.as_view(), name='detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='list'),
]
