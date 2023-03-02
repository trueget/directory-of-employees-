from django.shortcuts import render, redirect
from django.views.generic import ListView

from django.views import View

from .models import Employees
from .forms import EmployeesForm


# Create your views here.


class INdex(View):
    form_class = EmployeesForm
    initial = {'key': 'value'}
    template_name = 'index.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, self.template_name, {'form': form})


class AllWorkersListVew(ListView):
    model = Employees
    template_name = 'all_workers.html'
    context_object_name = 'all_workers'
    paginate_by = 500
