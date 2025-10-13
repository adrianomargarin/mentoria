from django.urls import path
from mentoria.blog.views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('<slug:category_slug>/<slug:post_slug>/', PostDetailView.as_view(), name='detail'),
    path('', PostListView.as_view(), name='index'),
]
