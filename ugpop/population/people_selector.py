from .models import Register_People

def get_Peoples():
    return Register_People.objects.all()

def get_people(people_ID):
    return Register_People.objects.get(pk=people_ID)

def auto_id_number():
    id_number = Register_People.objects.all().count()

    return f"{(id_number+1):05}"