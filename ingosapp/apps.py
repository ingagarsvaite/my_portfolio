from django.apps import AppConfig

class IngosappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ingosapp'
    verbose_name = 'My App'

    # def ready(self):
    #     import ingosapp.signals
