from django.contrib import admin
from mentoria.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): ...
