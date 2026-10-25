from django.apps import AppConfig

class JobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobs'

    def ready(self):
        import os
        
        if os.environ.get('RUN_MAIN', None) == 'true':
            from . import updater
            updater.start_scheduler()