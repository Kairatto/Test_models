from django.db import models
from slugify import slugify


class Tour(models.Model):
    title_tour = models.CharField(max_length=200, verbose_name='Название тура')
    text_tour = models.TextField()
    slug = models.SlugField(max_length=200, primary_key=True)

    def __str__(self) -> str:
        return self.title_tour

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_tour)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Days(models.Model):
    title_days = models.CharField(max_length=100, verbose_name='Название дня')
    description_days = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, primary_key=True)
    day = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='days',
    )

    def __str__(self) -> str:
        return self.title_days

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_days)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class DaysImage(models.Model):
    image = models.ImageField(upload_to='days_images')
    day = models.ForeignKey(
        to=Days,
        on_delete=models.CASCADE,
        related_name='days_images',
        null=True,
        blank=True,
        default=None
    )
