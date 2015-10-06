from django.db import models
from django.utils import timezone

def upload_to(instance, filename):
    return '%s/%s' % (timezone.now().strftime('%d%m%Y'), filename)

class Image(models.Model):
    name = models.CharField(max_length=50)
    source_file = models.ImageField(blank=False, upload_to=upload_to)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    caption=models.CharField(max_length=70, blank=True,)

    def clean(self, *args, **kwargs):
        self.source_file.name = self.source_file.name.encode('ascii','ignore')
        return super(Image, self).clean(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def image_thumbnail(self):
        return '<img src="%s" width="50" height="50" />' % (self.source_file.url)
    image_thumbnail.allow_tags = True