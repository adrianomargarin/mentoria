from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mentoria.profiles'

    def ready(self):
        from . import signals
        # signals.post_save_create_user_profile()