from django.contrib import admin
from .models import *


class CrafterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'logo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


admin.site.register(Crafter, CrafterAdmin)
