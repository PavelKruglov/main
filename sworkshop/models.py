from django.db import models


class Price(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, verbose_name='Цена')

    class Meta:
        verbose_name = ' Прайс '
        verbose_name_plural = 'Прайс'

    def __str__(self):
        return self.name


class News(models.Model):
    # id = models.IntegerField(primary_key=True, db_index=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(max_length=1500, blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='media/')
    link = models.CharField(max_length=1500, blank=True, null=True, verbose_name='Ссылка')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = ' Новости '
        verbose_name_plural = 'Новости'
        ordering = ['-published']

        def __str__(self):
            return self.id
