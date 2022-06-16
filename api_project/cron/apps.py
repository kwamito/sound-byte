from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CronConfig(AppConfig):
    name = "api_project.cron"
    verbose_name = _("Cron")
