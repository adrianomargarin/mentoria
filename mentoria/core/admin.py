from django.contrib import admin
from mentoria.core.models import Teste


@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'uuid', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['id', 'name']
