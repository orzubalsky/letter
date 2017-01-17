from django.contrib import admin
from tinymce.widgets import TinyMCE
from basic.admin import *
from letters.models import *


class SignatureInline(admin.TabularInline):
    """
    """
    model = Signature
    fields = (
        'person',
        'comment',
        'is_active'
    )
    extra = 0


class SignatureAdmin(BasicAdmin):
    fields = (
        'person',
        'letter',
        'comment',
    )
    list_display = (
        'person',
        'letter',
        'created',
        'is_active'
    )


class LetterAdmin(BasicAdmin):
    fieldsets = (
        ('Info', {
            'fields': (
                'title',
                'slug',
                'body',
                'date_published',
                'is_active'
            )
        }),
        ('Settings', {
            'fields': (
                'color',
                'do_color_inverse',
                'do_get_signatures',
                'do_show_signatures',
                'related_events',
                'related_letters',
            )
        }),
    )
    list_display = (
        'title',
        'color',
        'do_color_inverse',
        'do_get_signatures',
        'do_show_signatures',
        'is_active'
    )
    list_editable = (
        'color',
        'do_color_inverse',
        'do_get_signatures',
        'do_show_signatures',
        'is_active',
    )
    prepopulated_fields = {'slug': ('title',)}
    # inlines = (SignatureInline, )


admin.site.register(Letter, LetterAdmin)
admin.site.register(Signature, SignatureAdmin)
