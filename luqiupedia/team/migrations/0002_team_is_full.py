# Generated by Django 4.1 on 2022-08-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_full',
            field=models.BooleanField(default=False),
        ),
    ]
