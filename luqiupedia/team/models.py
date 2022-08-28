from django.db import models
# from player.models import Player

class Team(models.Model):
    class Tiers(models.TextChoices):
        tier_one = '1', 'Tier 1'
        tier_two = '2', 'Tier 2'
        tier_three = '3', 'Tier 3'

    class Regions(models.TextChoices):
        east_europe = 'EEU', 'East Europe'
        west_europe = 'WEU', 'West Europe'
        south_america = 'SA', 'South America'
        north_america = 'NA', 'North America'
        china = 'CH', 'China'
        southeast_asia = 'SEA', 'Southeast Asia'

    name = models.CharField(max_length=20)
    region = models.CharField(choices=Regions.choices, max_length=3)
    tier_level = models.CharField(choices=Tiers.choices, max_length=1)
    is_full = models.BooleanField(default=False)
    team_captain = models.OneToOneField(
        to='player.Player',
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.name)