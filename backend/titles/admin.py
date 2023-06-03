from django.contrib import admin
from .models import Title, Human, Place


class TitleAdmin(admin.ModelAdmin):
    pass


class HumanAdmin(admin.ModelAdmin):
    pass


class PlaceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Title, TitleAdmin)
admin.site.register(Human, HumanAdmin)
admin.site.register(Place, PlaceAdmin)
