from django.contrib import admin
from mentoria.blog.models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ['title']}
    filter_horizontal = ['tags']
    