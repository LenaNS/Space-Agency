from django.contrib.admin import ModelAdmin, register
from django.utils.html import mark_safe
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer
from .models import *


@register(Slider)
class ProductAdmin(SortableAdminMixin, ModelAdmin):
    """
    Панель администрирования слайдера.

    Поля
    ----
    list_display:
        Список отображаемых полей.
    """

    list_display = ("name", "image_tag", "sorting")

    def image_tag(self, obj):
        """
        Отображает миниатюру изображения для объекта Slider в административной панели.
        """
        if obj.image:
            thumbnailer = get_thumbnailer(obj.image)
            thumbnail = thumbnailer.get_thumbnail({
                'size': (50, 50),          
                'crop': True,           
                'quality': 90,          
            })
            return mark_safe(f'<img src="{thumbnail.url}" /> ')
        return "-"

    image_tag.short_description = "Картинка"

    class Media:
        js = ("adminsortable2/js/adminsortable2.min.js",)
