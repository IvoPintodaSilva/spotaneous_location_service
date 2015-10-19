from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from interests.models import Interest



class CustomUser(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.PointField(blank=True, null=True)
    interests = models.ManyToManyField(Interest, blank=True)
    ranking = models.IntegerField(default=0)
    objects = models.GeoManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __unicode__(self):
        return str(self.id)

    def get_user_location(self):
        return self.location

    def get_user_interests(self):
        return self.interests

    def get_user_ranking(self):
        return self.ranking
