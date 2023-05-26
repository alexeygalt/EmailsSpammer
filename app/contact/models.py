from django.db import models


class Contact(models.Model):
    """подписка на email"""

    name = models.CharField("Имя", max_length=32)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
