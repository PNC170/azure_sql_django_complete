from django.apps import AppConfig


class ApiConfig(AppConfig):
    # switch back to BigAutoField for large primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
