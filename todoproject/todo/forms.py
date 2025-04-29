from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.TextInput(attrs={
                'placeholder': 'YYYY-MM-DD HH:MM:SS',
                'class': 'w-full p-2 border border-gray-300 rounded'
            }),
        }
