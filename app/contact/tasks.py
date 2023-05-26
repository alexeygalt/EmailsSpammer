from django.core.mail import send_mail

from main.celery import app
from .models import Contact
from .service import send
from main import settings


@app.task
def send_spam_mail(user_mail):
    send(user_mail)


@app.task
def send_beat_mail():
    for contact in Contact.objects.all():
        send_mail(
            "Вы подписались на рассылку",
            "Мы будем присылать Вам много спама каждые 5м",
            settings.EMAIL_HOST_USER,
            [contact.email],
            fail_silently=False,
        )
