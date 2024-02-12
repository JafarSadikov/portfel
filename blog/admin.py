from django.contrib import admin
from .models import Clients


@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    prepopulated_fields = {'slug':('name',)}
