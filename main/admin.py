from django.contrib import admin
from .models import Conc


# Register your models here.
class ConcAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'dt')
    list_display_links = ('id', 'title')
    list_editable = ('dt',)


admin.site.register(Conc, ConcAdmin)
