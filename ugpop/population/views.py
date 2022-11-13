from django.shortcuts import render


from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,reverse
from django.contrib import messages
 


from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required 


from .people_selector import get_Peoples,get_people
from .register_people_form import PeopleForm

from .vht_selector import get_VHTS,get_VHT
from .register_vht_form import VHTForm

from .birth_selector import get_births,get_birth
from .register_birth_form import BirthForm

from .death_selector import get_deaths,get_death
from .report_death_form import DeathForm


import datetime

# user defined
from population.models import Register_VHT,Register_People,Register_Birth,Report_Death
from .register_vht_form import VHTForm
from .register_people_form import PeopleForm
from .register_birth_form import BirthForm
from .report_death_form import DeathForm

from .vht_selector import get_VHT, get_VHTS,generate_auto_serialnumber
from .people_selector import get_people, get_Peoples
from .birth_selector import get_birth, get_births
from .death_selector import get_death, get_deaths




# def index_view(request):

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index_page')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:
        return render (request,'login.html') 
        
#     return render(request, "index.html")
def index_page_view(request):
    return render(request, "login.html")



# Create your views here.


def index_page(request):
    VHTIDN = generate_auto_serialnumber()
    yea = datetime.datetime.today().year
    request_serial_number = f"VHT/UGLP/{yea}/{VHTIDN}"

    vht_form = VHTForm(initial={"VHTIDN": request_serial_number})
    get_vhts = get_VHTS()
    #auto no ends

    # get_vhts = get_VHTS()
    # vht_form= VHTForm()
    if request.method == "POST":
        vht_form=VHTForm(request.POST,request.FILES)
        if vht_form.is_valid():
            vht_form.save()
            messages.success(request,'VHT data submitted successfully')
        # else:
        #     messages.WARNING(request, 'Data submission failed' ) 
        
        return HttpResponseRedirect(reverse(index_page))

    context={
        "vht_form":vht_form,
        "get_vhts": get_vhts,
       
    }
    return render(request,"vht.html",context)



def vht_edit(request,VHT_ID):
    get_vht = get_VHT(VHT_ID)
    vht_form= VHTForm(instance = get_vht)
    if request.method == "POST":
        vht_form=VHTForm(request.POST,request.FILES, instance = get_vht)
        if vht_form.is_valid():
            vht_form.save()
            messages.success(request,'VHT changed successfully')
        else:
            messages.WARNING(request, 'Data change failed') 
            messages.error(request, 'Data change failed') 

            return HttpResponseRedirect(reverse(index_page))
    context={
        "vht_form":vht_form,
        "get_vht":get_vht
        
    }
    return render(request,"vht_edit.html",context)



def delete_VHT(request, VHT_ID):
    get_vht = get_VHT(VHT_ID)
    get_vht.delete()
    messages.info(request, "VHT deleted succesful")
    return redirect(index_page)
  


# Create your views here.

def people_page(request):

    UPIDN = generate_auto_serialnumber()
    yea = datetime.datetime.today().year
    ug_idno = f"UGP/{yea}/{UPIDN}"

    people_form = PeopleForm(initial={"UPIDN": ug_idno})
    get_ppls = get_Peoples()
    if request.method == "POST":
        people_form=PeopleForm(request.POST,request.FILES)
        if people_form.is_valid():
            people_form.save()
            messages.success(request,'data submitted successfully')
        else:
            messages.WARNING(request, 'Data submission failed...')
        
    context={
        "people_form":people_form,
        "get_ppls":get_ppls
    }
    return render(request,"people.html",context)

def edit_person_details(request, people_ID):
    getppl= get_people(people_ID)
    ppl_form = PeopleForm(instance = getppl)
    if request.method == "POST":
        ppl_form = PeopleForm(request.POST, request.FILES,instance = getppl)
        if ppl_form.is_valid():
            ppl_form.save()
            messages.success(request,'Persons_details Updated successfully....')
        else:
            messages.warning(request,'operation not successful')
        return HttpResponseRedirect(reverse(people_page))

    context={
        "ppl_form": ppl_form,
        "getppl": getppl
    }        
            
    return render(request,"ppl_edit.html",context)  

def delete_people(request, people_ID):
    ppl_del = get_people(people_ID)
    ppl_del.delete()
    messages.success(request,'Person details deleted successfully')
    return HttpResponseRedirect(reverse(people_page))

def birth_page(request):
    get_bbys = get_births()
    birth_form= BirthForm()
    if request.method == "POST":
        birth_form=BirthForm(request.POST,request.FILES)
        if birth_form.is_valid():
            birth_form.save()
            messages.success(request,'Birth Registration  successful.....')
        else:
            messages.WARNING(request, 'Data submission failed...')
        
                   

    context={
        "birth_form":birth_form,
        "get_bbys":get_bbys
    }
    return render(request,"birth.html",context)

def edit_birth(request, birth_ID):
    getbaby = get_birth(birth_ID)
    birthform = BirthForm(instance = getbaby)
    if request.method == "POST":
        birthform = BirthForm(request.POST, request.FILES,instance = getbaby)
        if birthform.is_valid():
            birthform.save()
            messages.success(request,'Birth Data updated successfully.....')
        else:
            messages.warning(request,'operation not successful')
        return HttpResponseRedirect(reverse(birth_page))

    context={
        "birthform": birthform,
        "getbaby": getbaby
    }        
            
    return render(request,"birth_edit.html",context)  


def delete_birth(request, birth_ID):
    birth_del = get_birth(birth_ID)
    birth_del.delete()
    messages.success(request,'Birth record deleted successfully')
    return HttpResponseRedirect(reverse(birth_page))
    

def birth_report(request):
    
    get_birth_report = get_births()

    context={
        "get_birth_report": get_birth_report
    }        
    return render(request, "birth_report.html",context)


#death page

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='death').exists(),login_url='login') 
def death_page(request):
    get_deads = get_deaths()
    death_form= DeathForm()
    if request.method == "POST":
        death_form=DeathForm(request.POST,request.FILES)
        if death_form.is_valid():
            death_form.save()
            messages.success(request,'Death Registered  successful.....')
        else:
            messages.WARNING(request, 'Data submission failed...')
        
    context={
        "death_form":death_form,
        "get_deads":get_deads
    }
    return render(request,"death.html",context)


# generating report for death rate
def death_report(request):
    
    get_death_report = get_deaths()

    context={
        "get_death_report": get_death_report
    }        
    return render(request, "death_report.html",context)


def delete_death(request, death_ID):
    death_del = get_death(death_ID)
    death_del.delete()
    messages.success(request,'Death record deleted successfully')
    return HttpResponseRedirect(reverse(birth_page))

def death_edit(request,death_ID):
    get_dead = get_death(death_ID)
    dead_form= DeathForm(instance = get_dead)
    if request.method == "POST":
        dead_form=DeathForm(request.POST,request.FILES, instance = get_dead)
        if dead_form.is_valid():
            dead_form.save()
            messages.success(request,'VHT changed successfully')
        else:
            messages.WARNING(request, 'Data change failed') 
            messages.error(request, 'Data change failed') 

            return HttpResponseRedirect(reverse(death_page))
    context={
        "dead_form":dead_form,
        "get_dead":get_dead
        
    }
    return render(request,"death_edit.html",context)