from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, objects):
        return format_html("<img src='{}' width=40 style='border-radius:50px' />".format(objects.featured_photo.url))

    thumbnail.short_description = "photo"

    list_display = (
        'id', 'thumbnail', 'car_name', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_name')
    search_fields = ('car_name', 'color', 'model', 'city')
    list_filter = ('model','city', 'body_style',)
    list_editable = ('is_featured',)


admin.site.register(Car, CarAdmin)
