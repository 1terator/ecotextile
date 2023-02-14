import os

from celery import Celery

import ecotextile.settings as settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecotextile.settings")

app = Celery("celery_django")
app.config_from_object(settings)
app.autodiscover_tasks()
