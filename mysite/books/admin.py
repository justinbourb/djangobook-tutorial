from django.contrib import admin
from .models import Publisher, Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    search_fields = ('title', 'publisher__name', 'publication_date')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    '''sets fields the admin can edit or not(by not adding to this list)'''
    #fields = ('title', 'authors', 'publisher', 'publication_date')
    #filter_vertical = ('authors',)
    '''changes the publisher field from a drop down menu to raw_id_field because
    raw id loads faster'''
    raw_id_fields = ('publisher',)



    
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
