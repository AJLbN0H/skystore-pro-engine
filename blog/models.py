from django.db import models


class BlogEntry(models.Model):

    title = models.CharField(
        max_length=150, verbose_name="Заголовок"
    )

    content = models.TextField(
        verbose_name="Содержимое"
    )

    preview = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
        verbose_name="Превью"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    publication_sign = models.BooleanField(
        default=False,
        verbose_name='Опубликовать?'
    )

    number_of_views = models.IntegerField(default=0, blank=True,
        null=True,)

    class Meta:
        verbose_name = "Запись в блог"
        verbose_name_plural = "Записи в блог"
        ordering = ["title", "number_of_views"]

    def __str__(self):
        return f'{BlogEntry.title}'

