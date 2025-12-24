from django.contrib import admin
from .models import ListItem, TodoList



@admin.register(TodoList)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name','is_priority')


@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ('title','notification_date')