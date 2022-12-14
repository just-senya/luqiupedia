# Generated by Django 4.1 on 2022-08-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_nickname_alter_player_team_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='approx_total_winnings',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='fullname',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
