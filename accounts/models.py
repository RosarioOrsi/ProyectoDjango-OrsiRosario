from django.db import models
from django.contrib.auth.models import AbstractUser

#Donde se guardan los avatars
def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

#Usuario personalizado
class Perfil(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        default="default/avatar.png",
        blank=True,
        null=True,
        verbose_name="Avatar"
    )

    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")
    fecha_de_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username