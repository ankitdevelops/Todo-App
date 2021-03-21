from django import forms
from django.forms import ModelForm, fields, models
from . models import Todo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['user']