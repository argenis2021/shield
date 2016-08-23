from django.contrib import admin
from shield.models import Heroe, Poder
from shield.models import Equipo, Avistamiento

class HeroeAdmin(admin.ModelAdmin):
    search_fields = ('nombre_heroe', 'identidad',
        'poderes__nombre_poder')
    list_display = ('nombre_heroe', 'identidad',
        'nivel', 'lista_poderes', 'equipo')
    list_filter = ('equipo','poderes__nombre_poder')
admin.site.register(Heroe, HeroeAdmin)

 #admin.site.register(Heroe)
admin.site.register(Poder)
admin.site.register(Equipo)
admin.site.register(Avistamiento)
