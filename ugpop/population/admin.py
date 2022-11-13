from django.contrib import admin
from .models import Register_VHT,Register_People,Register_Birth,Report_Death

# Register your models here.

admin.site.site_header = "UGLP Admin"
admin.site.site_title = "Ug Popoulation"
admin.site.index_title = "Welcome to Ug Live Population "


admin.site.register(Register_VHT),
admin.site.register(Register_People),
admin.site.register(Register_Birth),
admin.site.register(Report_Death)