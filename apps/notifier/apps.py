from django.apps import AppConfig


class NotifierConfig(AppConfig):
    name = 'apps.notifier'

    def ready(self):
        from apps.notifier.tasks import register_models
        register_models() # Here!