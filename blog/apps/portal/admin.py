from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class CategoryResource(resources.ModelResource):
    class Meta:
        model: Category

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','state','date_creation',)
    resource_class = CategoryResource

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name','last_name','email']
    list_display = ('name','last_name','email','state','date_creation',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
