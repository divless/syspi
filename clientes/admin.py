from django.contrib import admin
from .models import Cliente, Ficha, Contrato, Plano

@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('name','email')
admin.site.register(Ficha)
admin.site.register(Contrato)
admin.site.register(Plano)
