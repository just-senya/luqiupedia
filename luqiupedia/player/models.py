from django.db import models
from django.utils.translation import gettext_lazy as _
# from team.models import Team


class Player(models.Model):
    class Nationality(models.TextChoices):
        kazakhstan = 'KZ', _('Kazakhstan')
        russia = 'RU', _('Russia')
        ukraine = 'UA', _('Ukraine')
        china = 'CH', _('China')
        israel = 'IL', _('Israel')
        france = 'FR', _('France')
        germany = 'DE', _('Germany')
        finland = 'FL', _('Finland')
        swedish = 'SE', _('Swedish')
        poland = 'PL', _('Poland')
        bulgaria = 'BG', _('Bulgaria')

    class Roles(models.TextChoices):
        Carry = '1', _('Carry')
        Midliner = '2', _('Midline')
        Offliner = '3', _('Offliner')
        SemiSupport = '4', _('SemiSupport')
        Support = '5', _('Support')
        Coach = '6', _('Coach')

    fullname = models.CharField(max_length=40, default=None)
    nickname = models.CharField(max_length=40, default=None)
    nationality = models.CharField(choices=Nationality.choices, max_length=2)
    birthdate = models.DateField()
    approx_total_winnings = models.IntegerField(null=True, blank=True, default=None)
    current_role = models.CharField(choices=Roles.choices, max_length=1)
    team_id = models.ForeignKey(to='team.Team', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.nickname)
