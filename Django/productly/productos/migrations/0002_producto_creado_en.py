# Generated by Django 5.0.3 on 2024-03-16 00:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]