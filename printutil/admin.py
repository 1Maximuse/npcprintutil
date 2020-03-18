from datetime import datetime
from django.contrib import admin

from .models import PrintRequest

def timestamp(obj):
    return obj.req_time.strftime("%d/%m/%Y, %H:%M:%S")

def set_printed(modeladmin, request, queryset):
    queryset.update(printed=True)
set_printed.short_description = "Mark selected as printed"

def set_notprinted(modeladmin, request, queryset):
    queryset.update(printed=False)
set_notprinted.short_description = "Mark selected as not printed"


class PrintRequestAdmin(admin.ModelAdmin):
    list_display = ('username', timestamp, 'printed')
    actions = [set_printed, set_notprinted]


admin.site.register(PrintRequest, PrintRequestAdmin)