from django.contrib import admin


from .models import WeakAura, WeakAuraData


class WeakAuraDataInline(admin.TabularInline):
    model = WeakAuraData
    extra = 1
    fieldsets = [
        (None,  {'fields': [('version', 'data')]})
    ]


class WeakAuraAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created',)
    fieldsets = [
        (None,          {'fields': ['title', 'description', 'author']}),
        ("Rarely Used", {'fields': ['datetime_created'],
                         'classes': ['collapse']}),
    ]
    inlines = [WeakAuraDataInline]


admin.site.register(WeakAura, WeakAuraAdmin)
admin.site.register(WeakAuraData)
