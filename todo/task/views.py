from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TodoListForm, ListItemForm
from .models import TodoList, ListItem


@login_required
def tasks(request):
    # 1. Загружаем только данные текущего пользователя
    todo_lists = TodoList.objects.filter(owner=request.user).order_by('-is_priority')
    list_items_form = ListItemForm()
    # Инициализируем форму (пустую для GET или заполненную для POST)
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.owner = request.user
            new_list.save()
    else:
        form = TodoListForm()
    if request.method == 'POST':
        list_items_form = ListItemForm(request.POST)
        if list_items_form.is_valid():
            list_items_form.save()
    else:
        list_items_form = TodoListForm()
    contexts = {
        "todo_list": todo_lists,
        "form": form,
    }
    return render(request, 'task/todo.html', contexts)