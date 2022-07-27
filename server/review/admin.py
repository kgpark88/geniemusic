from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Review

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Review._meta.fields]   
    list_filter = ['source',]
    search_fields = ['username', 'content']