# Generated by Django 4.1 on 2022-08-11 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_alter_player_current_role'),
        ('team', '0003_team_team_captain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_captain',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.player'),
        ),
    ]
