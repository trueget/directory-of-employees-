from django.forms import ModelForm
from .models import Employees


class EmployeesForm(ModelForm):

    class Meta:
        model = Employees
        # fields = ['first_name', 'last_name', 'sur_name', 'salary', 'job_title']
        fields = '__all__'