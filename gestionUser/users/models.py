from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("view_ventas", "Can view ventas section"),
            ("view_compras", "Can view compras section"),
            ("view_inventarios", "Can view inventarios section"),
        ]

