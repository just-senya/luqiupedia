# Generated by Django 4.1 on 2022-08-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourname', '0003_tourname_participants_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourname',
            name='total_dpc_points',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
