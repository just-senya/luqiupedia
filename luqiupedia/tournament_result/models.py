from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class TournameResult(models.Model):
    # results_of_tournament = models.OneToOneField(to='tourname.Tourname', on_delete=models.CASCADE)
    # participant_places = models.ManyToManyField(to='team.Team')
    participant_places = JSONField(default=dict)
    allocated_dpc_points = ArrayField(base_field=models.IntegerField())
    allocated_prize_pool = ArrayField(base_field=models.IntegerField())

    def __init__(self, results_of_tournament, allocated_dpc_points=None,
                 allocated_prize_pool=None, participant_places=None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        places = results_of_tournament.participants_number
        print("Look at here", places, '\n\n')
        self.results_of_tournament = results_of_tournament

        if allocated_prize_pool:
            self.allocated_prize_pool = allocated_prize_pool
        else:
            print(self.results_of_tournament.participants_number,
                  self.results_of_tournament.prize_pool, "look at here")
            first_place = int(self.results_of_tournament.prize_pool) / 2
            second_place = 3 * int(self.results_of_tournament.prize_pool) / 10
            third_place = int(self.results_of_tournament.prize_pool) - (first_place + second_place)

            self.allocated_prize_pool = [0 for _ in range(places)]
            self.allocated_prize_pool[0] = first_place
            self.allocated_prize_pool[1] = second_place
            self.allocated_prize_pool[2] = third_place

        if allocated_dpc_points:
            self.allocated_dpc_points = allocated_dpc_points
        else:
            self.allocated_dpc_points = [0 for _ in range(places)]

        if participant_places:
            self.participant_places = participant_places
        else:
            places = results_of_tournament.participant_numbers
            for place in range(places):
                self.participant_places[str(place+1)] = 'to be determined'

    def __str__(self):
        return str("Result of " + str(self.results_of_tournament.tourname))

    def __repr__(self):
        return str("something")
