# Generated by Django 4.0.1 on 2022-02-24 03:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cuerpo',
            field=tinymce.models.HTMLField(),
        ),
    ]
