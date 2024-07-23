# Generated by Django 4.1.13 on 2024-07-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_file',
        ),
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.URLField(default='https://cdn-1.webcatalog.io/catalog/wext/wext-icon-filled-256.png?v=1714780999610'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]