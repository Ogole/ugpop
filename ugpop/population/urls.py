from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import population.views as vs



urlpatterns = [
    
    
    
    path('', vs.login,name="login"),
    
    path('login', vs.login,name="login"),
    path('index_page/', vs.index_page, name='index_page'),
    path('people_page/', vs.people_page, name='people_page'),
    path('people_edit/<int:people_ID>/', vs.edit_person_details, name='people_edit'),
    path('delete_people/<int:people_ID>/', vs.delete_people, name="delete_people"),
    path('vht_edit/<int:VHT_ID>/', vs.vht_edit, name='vht_edit'),
    path('birth_page/', vs.birth_page, name='birth_page'),
    path('death_page/', vs.death_page, name='death_page'),
    path('delete_death/<int:death_ID>/', vs.delete_death, name="delete_death"),
    path('death_edit/<int:death_ID>/', vs.death_edit, name="death_edit"),
    path('edit_birth/<int:birth_ID>/', vs.edit_birth, name="edit_birth"),
    path('delete_birth/<int:birth_ID>/', vs.delete_birth, name="delete_birth"),
    path('delete_VHT/<int:VHT_ID>/', vs.delete_VHT, name='delete_VHT'),
    path('birth_report', vs.birth_report,name="birth_report"),
    path('death_report', vs.death_report,name="death_report"),

]