from django.apps import AppConfig


class AppPortofolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_portofolio'

    # Defining the ready method. This method is called once Django has carried out initialization tasks.
    def ready(self):
        # Importing the signals module from the app. This is typically where signal handlers are connected.
        # By doing this here, we ensure that our signal handlers are connected when the app is ready.
        import app_portofolio.signals
