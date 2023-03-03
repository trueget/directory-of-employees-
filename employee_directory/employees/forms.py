from django.forms import ModelForm
from .models import Employees
from django.forms import (
    ModelForm,
    TextInput,
    Select,
    NumberInput
)


class EmployeesForm(ModelForm):

    class Meta:
        model = Employees
        # fields = ['first_name', 'last_name', 'sur_name', 'salary', 'job_title']
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'id-first_name',
                # 'placeholder': '.'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'id-last_name',
            }),
            'salary': NumberInput(attrs={
                'class': 'form-control',
                'id': 'id-salary',
            }),
            'job_title': Select(attrs={
                'class': 'form-control',
                'id': 'id-job_title',
            }),
            'supervisor': Select(attrs={
                'class': 'form-control',
                'id': 'id-supervisor',
            })
        }