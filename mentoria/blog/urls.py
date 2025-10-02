from django.urls import path
from mentoria.blog.views import category_list, post_list_by_category, post_detail

app_name = 'blog'

urlpatterns = [
    path('<slug:category_slug>/', post_list_by_category, name='post-list-by-category'),
    path('<slug:category_slug>/<slug:post_slug>/', post_detail, name='post-detail'),
    path('', category_list, name='list'),

]