from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from interests.models import Interest



class CustomUser(AbstractUser):
    location = models.PointField(blank=True, null=True)
    interests = models.ManyToManyField(Interest, blank=True)
    ranking = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_user_location(self):
        return self.location

    def get_user_interests(self):
        return self.interests
