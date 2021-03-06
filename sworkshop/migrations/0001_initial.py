# Generated by Django 3.2.3 on 2021-08-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='media/')),
                ('link', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ссылка')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': ' Новости ',
                'verbose_name_plural': 'Новости',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Цена')),
            ],
            options={
                'verbose_name': ' Прайс ',
                'verbose_name_plural': 'Прайс',
            },
        ),
    ]
