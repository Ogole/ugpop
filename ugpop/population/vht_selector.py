from .models import Register_VHT

def get_VHTS():
    return Register_VHT.objects.all()

def get_VHT(VHT_ID):   
    return Register_VHT.objects.get(pk=VHT_ID)
     

def generate_auto_serialnumber():
    request_count = Register_VHT.objects.all().count()

    return f"{(request_count+1):04}"
