from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from mentoria.blog.models.post import Post


class PostListView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-published_by']

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=False)


class PostDetailView(DetailView):
    template_name = 'blog/post.html'

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=False)

    def get_object(self):
        return get_object_or_404(Post, category__slug=self.kwargs['category_slug'], slug=self.kwargs['post_slug'])
