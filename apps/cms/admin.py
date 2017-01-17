from django.contrib import admin
from basic.admin import *
from cms.models import *


class ContentBlockAdmin(BasicAdmin):
    fields = (
        'name',
        'position',
        'content',
        'slug',
        'is_active'
    )
    list_display = ('name', 'position', 'created', 'updated', 'is_active')
    list_editable = ('position', 'is_active',)
    prepopulated_fields = {'slug': ('name',)}


# register admin models
admin.site.register(ContentBlock, ContentBlockAdmin)
