# Generated by Django 5.1.1 on 2024-10-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news_post',
            name='name',
            field=models.TextField(verbose_name='Имя Автора/Авторки'),
        ),
    ]
