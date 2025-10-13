from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from mentoria.blog.models.post import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-published_by']

    def get_queryset(self):
        return Post.objects.filter(published_by__isnull=False)


def post_detail(request, category_slug, post_slug):
    post = get_object_or_404(Post, category__slug=category_slug, slug=post_slug)

    return render(request, 'blog/post.html', {'post': post})
