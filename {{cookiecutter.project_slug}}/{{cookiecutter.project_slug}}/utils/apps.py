import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UtilsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.project_slug }}.utils"
    verbose_name = _("Utilities")

    def ready(self):
        with contextlib.suppress(ImportError):
            import {{ cookiecutter.project_slug }}.utils.signals
