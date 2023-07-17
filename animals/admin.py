from django.contrib import admin

from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'countries']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Animal, AnimalAdmin)