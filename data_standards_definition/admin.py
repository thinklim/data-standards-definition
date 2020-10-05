from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Content, Document, DocumentCollection


@admin.register(Content)
class ContentAdmin(ImportExportModelAdmin):
    pass

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(DocumentCollection)
class DocumentCollectionAdmin(admin.ModelAdmin):
    pass