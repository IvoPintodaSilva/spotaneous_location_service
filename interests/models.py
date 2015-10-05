from django.db import models
from django.utils.translation import ugettext_lazy as _


class Interest(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = _("interest")
        verbose_name_plural = _("insterests")

    def __unicode__(self):
        return self.name
