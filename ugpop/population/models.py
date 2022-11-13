from django.db import models

# Create your models here.

import uuid

class Register_VHT(models.Model):
    VHTIDN=models.CharField(max_length=50)
    First_Name=models.CharField(max_length=50)
    Middle_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    GENDER_TYPE_CHOICES=[
        ('Male', 'Male'),
        ('Female','Female')
    ]
    Gender=models.CharField(choices=GENDER_TYPE_CHOICES, default='Male', max_length=10 )
    DOB=models.DateField(max_length=50)
    Phone_Number=models.CharField(max_length=15)
    Email_Address=models.CharField(max_length=50)
    Nationality=models.CharField(max_length=50)
    REGION_TYPE_CHOICES = [
        ('Central ','Central '),
        ('Northern','Northern'),
        ('West Nile','West Nile'),
        ('Western','Western'),
        ('Eastern','Eastern'),
    ]
    Region = models.CharField(choices=REGION_TYPE_CHOICES, default='Central',max_length=50)
    District = models.CharField(max_length=50)
    Constitutuency=models.CharField(max_length=100)
    SubCounty=models.CharField(max_length=50)
    Parish_or_Ward=models.CharField(max_length=50)
    Village_or_Zone=models.CharField(max_length=50)
    Occupation=models.CharField(max_length=50)

    def __str__ (self):
        return f'{self.Region}'

    
  
class Register_People(models.Model):
    UPIDN=models.CharField(max_length=50)
    First_Name=models.CharField(max_length=50)
    Middle_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    GENDER_TYPE_CHOICES=[
        ('Male', 'Male'),
        ('Female','Female')
    ]
    Gender=models.CharField(choices=GENDER_TYPE_CHOICES, default='Male', max_length=10 )
    DOB=models.DateField()
    MARITAL_TYPE_CHOICES=[
        ('Single','Single'),
        ('Married','Married'),
        ('Divorced','Divorced'),
    ]
    Marital_status=models.CharField(choices=MARITAL_TYPE_CHOICES, default='Single', max_length=20)
    disability_type_choices=[
        ('None','None'),
        ('Deaf','Deaf'),
        ('Cripple','Cripple'),
    ]
    Disability=models.CharField(choices=disability_type_choices, default='None', max_length=20)
    Nationality=models.CharField(max_length=50)
    Region=models.ForeignKey(Register_VHT, on_delete=models.CASCADE)
    District = models.CharField(max_length=50)
    Constitutuency=models.CharField(max_length=100)
    SubCounty=models.CharField(max_length=50)
    Parish_or_Ward=models.CharField(max_length=50)
    Village_or_Zone=models.CharField(max_length=50)
    Occupation=models.CharField(max_length=50)


class Register_Birth(models.Model):
    Birth_Certificate_Number=models.UUIDField(default=uuid.uuid4,editable=False)
    First_Name=models.CharField(max_length=50)
    Middle_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    GENDER_TYPE_CHOICES=[
        ('Male', 'Male'),
        ('Female','Female')
    ]
    Gender=models.CharField(choices=GENDER_TYPE_CHOICES, default='Male', max_length=10 )
    DOB=models.DateField()
    Place_of_Birth=models.CharField(max_length=50)
    Nationality=models.CharField(max_length=50)
    Region=models.ForeignKey(Register_VHT, on_delete=models.CASCADE)
    District = models.CharField(max_length=50)
    Constitutuency=models.CharField(max_length=100)
    SubCounty=models.CharField(max_length=50)
    Parish_or_Ward=models.CharField(max_length=50)
    Village_or_Zone=models.CharField(max_length=50)

    def __str__ (self):
        return f'{self.Gender}'

class Report_Death(models.Model):
    Enter_IDNO=models.CharField(max_length=20)
    First_Name=models.CharField(max_length=50)
    Middle_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Gender = models.ForeignKey(Register_Birth, on_delete=models.CASCADE, null=True)
    Date_of_Death=models.DateField()
    Region=models.ForeignKey(Register_VHT, on_delete=models.CASCADE)
    District = models.CharField(max_length=50)
    Constitutuency=models.CharField(max_length=100)
    SubCounty=models.CharField(max_length=50)
    Parish_or_Ward=models.CharField(max_length=50)
    Village_or_Zone=models.CharField(max_length=50)




    
   