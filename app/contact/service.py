from django.core.mail import send_mail
from main import settings


def send(user_mail):
    send_mail(
        "Вы подписались на рассылку",
        "Мы будем присылать Вам много спама",
        settings.EMAIL_HOST_USER,
        [user_mail],
        fail_silently=False,
    )
