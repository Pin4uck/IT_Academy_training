from django.contrib import admin
from .models import Notes


class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'data')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'data')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'content', 'data')


admin.site.register(Notes, NotesAdmin)
