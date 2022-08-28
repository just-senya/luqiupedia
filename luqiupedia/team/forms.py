from django.forms import ModelForm
from .models import Team

class TeamForm(ModelForm):
    model = Team
    fields = '__all__'
