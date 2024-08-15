from django.apps import AppConfig


class PrintConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Print'

    def ready(self):
        import Print.singals