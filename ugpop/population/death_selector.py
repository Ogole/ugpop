from .models import Report_Death

def get_deaths():
    return Report_Death.objects.all()

def get_death(death_ID):
    return Report_Death.objects.get(pk=death_ID)
    