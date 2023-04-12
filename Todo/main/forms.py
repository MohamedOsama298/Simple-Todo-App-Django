from django.forms import ModelForm, TextInput

from .models import Todo, TodoItems
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class' : 'form-control',
            })
        }

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']
        
class TodoItemsForm(ModelForm):
    class Meta:
        model = TodoItems
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            })
        }