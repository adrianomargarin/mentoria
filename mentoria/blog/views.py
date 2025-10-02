from django.shortcuts import render, get_object_or_404
from mentoria.blog.models.category import Category
from mentoria.blog.models.post import Post


def category_list(request):
    categories = Category.objects.all()

    return render(request, 'blog/category_list.html', {'categories': categories})


def post_list_by_category(request, category_slug):
    posts = Post.objects.filter(category__slug=category_slug)

    return render(request, 'blog/post_list_by_category.html', {'posts': posts})


def post_detail(request, category_slug, post_slug):
    post = get_object_or_404(Post, category__slug=category_slug, slug=post_slug)

    return render(request, 'blog/post_detail.html', {'post': post})
