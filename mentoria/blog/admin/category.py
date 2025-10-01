from django.contrib import admin
from mentoria.blog.models.category import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ['name']}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'slug']