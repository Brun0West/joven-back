from django.contrib import admin

from .models import Mensaje, Categoria

admin.site.site_header = 'Administracion de Las Penas de Bruno'



class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre_tipo')
    search_fields = ('nombre_tipo',)

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('id_escrito', 'titulo', 'id_categoria', 'fecha')
    list_display_links = ('titulo', 'id_categoria', 'fecha')
    search_fields = ('titulo', 'id_categoria', 'fecha')
    list_filter = ('id_categoria', 'fecha')

admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Categoria, CategoriaAdmin)