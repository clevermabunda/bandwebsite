from django.apps import AppConfig

class ThebandConfig(AppConfig):
    """
    Configuration for the 'theband' Django application.

    This class is used to configure the app, including setting the 
    default auto field type for model primary keys.

    Attributes:
        default_auto_field (str): The default type for auto-generated 
        primary keys in models. Set to 'BigAutoField'.
        name (str): The name of the application. Used by Django to 
        identify the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theband'
