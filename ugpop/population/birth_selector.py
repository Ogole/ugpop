from .models import Register_Birth

def get_births():
    return Register_Birth.objects.all()

def get_birth(birth_ID):
    return Register_Birth.objects.get(pk=birth_ID)


