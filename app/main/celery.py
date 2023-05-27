import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
app = Celery("main")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-spam-every-1-minute": {
        "task": "contact.tasks.send_beat_mail",
        "schedule": crontab(minute="*/20"),
    },
}
