# Generated by Django 4.0.4 on 2022-08-17 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_result', '0003_rename_tourname_tournameresult_results_of_tournament_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournameresult',
            name='results_of_tournament',
        ),
    ]
