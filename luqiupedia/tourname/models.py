from django.db import models


from tournament_result.models import TournameResult


class Tourname(models.Model):
    class TournamentType(models.TextChoices):
        online = 'online', 'Online'
        offline = 'offline', 'Offline'

    class Tiers(models.TextChoices):
        tier_one = '1', 'Tier 1'
        tier_two = '2', 'Tier 2'
        tier_three = '3', 'Tier 3'

    tourname = models.CharField(max_length=60)
    organizer = models.CharField(max_length=60)
    tournament_type = models.CharField(max_length=7, choices=TournamentType.choices)
    prize_pool = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(to='team.Team')
    participants_number = models.IntegerField(default=0)
    tier_level = models.CharField(choices=Tiers.choices, max_length=1)
    description = models.CharField(max_length=250, blank=True, null=True)
    total_dpc_points = models.IntegerField(default=0, null=True)
    tournament_result_table = models.OneToOneField(to='tournament_result.TournameResult',
                                                   on_delete=models.CASCADE,
                                                   default=None)

    @classmethod
    def create(cls, self, tourname=None, organizer=None, tournament_type=None,
               prize_pool=None, start_date=None, end_date=None,
               tier_level=None, participants_number=None,
               description=None, total_dpc_points=0,
               *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tourname = tourname
        self.organizer = organizer
        self.tournament_type = tournament_type
        self.participants_number = participants_number
        self.prize_pool = prize_pool
        self.start_date = start_date
        self.end_date = end_date
        self.tier_level = tier_level
        self.description = description
        self.total_dpc_points = total_dpc_points
        self.tournament_result_table = TournameResult(self)
        self.tournament_result_table.save()

    def __str__(self):
        return str(self.tourname)
