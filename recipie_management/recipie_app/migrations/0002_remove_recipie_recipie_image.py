# Generated by Django 5.2 on 2025-04-03 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipie',
            name='recipie_image',
        ),
    ]
