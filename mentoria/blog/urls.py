from django.urls import path
from mentoria.blog.views import PostListView, post_detail

app_name = 'blog'

urlpatterns = [
    path('<slug:category_slug>/<slug:post_slug>/', post_detail, name='detail'),
    path('', PostListView.as_view(), name='index'),
]
