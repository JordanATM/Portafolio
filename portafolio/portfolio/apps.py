from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"
    verbose_name = "Portafolio" #Configuracion extendida para cambiar nombre de app en panel administración 
 