from django import forms
from .models import TodoList, ListItem

class TodoListForm(forms.ModelForm):
    class Meta: 
        model = TodoList
        fields = ['name', 'desc', 'is_priority']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inp-basic', 'placeholder': 'Название списка'}),
            'desc': forms.Textarea(attrs={'class': 'inp-basic', 'rows': 3, 'placeholder': 'Описание...'}),
            'is_priority': forms.CheckboxInput(attrs={'class': 'chx-basic'}),
        }

class ListItemForm(forms.ModelForm):
    class Meta: 
        model = ListItem
        fields = ['title', 'detail', 'is_priority', 'notification_date', 'notification_repeat']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'label':"Название",
                "placeholder": "Введите название",
                "class": "inp-basic"
            }),
            'detail': forms.Textarea(attrs={
                "placeholder": "Введите детали (мотивация)",
                "class": "inp-basic",
                "rows": 4
            }),
            'is_priority': forms.CheckboxInput(attrs={
                'class': "chx-basic"
            }),
            
            'notification_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                "class": "inp-basic",
                "type": "datetime-local"
            }),
            'notification_repeat': forms.CheckboxInput(attrs={
                "class": "chx-basic"
            })
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Это заставит Django принимать формат из HTML5 календаря
        self.fields['notification_date'].input_formats = ['%Y-%m-%dT%H:%M']