from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TodoListForm, ListItemForm
from .models import TodoList, ListItem


@login_required()
def tasks(request):
    todo_lists = TodoList.objects.order_by('-is_priority')
    if request.method == 'POST':
        pass

    contexts = {
        "todo_list": todo_lists
    }
    return render(request, 'task/todo.html', contexts)