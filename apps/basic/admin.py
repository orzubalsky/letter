from django.contrib import admin
from basic.models import Person


class BasicAdmin(admin.ModelAdmin):
    """
    """
    pass


class PersonInline(admin.TabularInline):
    """
    """
    model = Person
    fields = (
        'name',
        'email',
        'is_active'
    )
    extra = 0


class PersonAdmin(BasicAdmin):
    fields = ('name', 'email')
    list_display = ('name', 'email', 'created', 'is_active')
    list_editable = ('is_active', 'email')


# register admin models
admin.site.register(Person, PersonAdmin)
