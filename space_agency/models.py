from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    """
    Модель слайдера.

    Поля
    ----
    name:
        Название картинки.
    image:
        Картинка.
    sorting:
        Порядковый номер записи.
    """

    name = models.CharField(max_length=255, verbose_name="Имя картинки")
    image = FilerImageField(
        related_name="slider_images",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Картинка",
    )
    sorting = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["sorting"]
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        
