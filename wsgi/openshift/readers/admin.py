from django.contrib import admin
from readers.models import Reader

# Register your models here.
class ReaderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info',
         {'fields' : ['raw_file', 'analyzed_data']})
        ]
    list_display = ('raw_file',)
    list_filter = ['raw_file']
    search_fields = ['raw_file']

admin.site.register(Reader, ReaderAdmin)
