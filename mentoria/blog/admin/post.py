from datetime import datetime
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from mentoria.blog.models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'slug', 'created_by', 'published_by', 'published_at', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ['title']}
    filter_horizontal = ['tags']
    actions = ['action_publish']
    readonly_fields = ['created_by', 'published_by', 'published_at']

    @admin.display(description=_('publish'))
    def action_publish(self, request, queryset):
        queryset = queryset.filter(published_at__isnull=True)
        count = queryset.count()
        queryset.update(published_by=request.user, published_at=datetime.now())

        self.message_user(request, f'{count} POSTs publicados.')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user

        return super().save_model(request, obj, form, change)
