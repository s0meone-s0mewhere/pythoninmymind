# Generated by Django 5.0.1 on 2024-01-29 19:02

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
