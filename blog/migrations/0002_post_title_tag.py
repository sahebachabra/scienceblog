# Generated by Django 4.2.17 on 2025-01-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='The Axon Journal', max_length=255),
        ),
    ]
