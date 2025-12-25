from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=252)
    desc = models.TextField(max_length=300, null=True, blank=True)
    is_priority = models.BooleanField(default=False)
    def __str__(self):
        return self.name




class ListItem(models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE , related_name='items')
    title = models.CharField(max_length=300)
    detail = models.TextField(null=True, blank=True)
    is_priority = models.BooleanField(default=False)
    notification_date = models.DateTimeField( null=True, blank=True)
    notification_repeat = models.BooleanField(default=False)
    def __str__(self):
        return self.title

