# Generated by Django 4.0.2 on 2022-03-17 04:10

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generateUniqueCode, max_length=8, unique=True),
        ),
    ]
