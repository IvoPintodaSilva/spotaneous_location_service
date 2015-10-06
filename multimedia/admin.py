from django.contrib import admin
from multimedia.models import Image

class ImageAdmin(admin.ModelAdmin):
    model = Image
    search_fields = ('name',)
    list_display= ('name', 'image_thumbnail',)

admin.site.register(Image, ImageAdmin)