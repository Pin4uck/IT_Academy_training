from django.db import models


class Notes(models.Model):
    objects = None
    title = models.CharField('Название', max_length=60)
    slug = models.SlugField('Slug', max_length=60, unique=True, db_index=True)
    content = models.TextField('Контент', blank=True)
    data = models.DateTimeField('Дата создания')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/notebook/note-{self.id}'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
