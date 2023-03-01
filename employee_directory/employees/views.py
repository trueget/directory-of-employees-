from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView

from django.views import View
from django.http import HttpResponseRedirect

from .models import Employees
from .forms import EmployeesForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


class Index(DetailView):
    model = Employees
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_workers'] = Employees.objects.all()
        context['form'] = EmployeesForm()
        return context

    def post(self):
        if self.request.method == 'POST':
            en_form = EmployeesForm(self.request.POST)
            if en_form.is_valid():
                print('-' * 50)
                print(en_form)
            else:
                print('-' * 50)
                print('не валидна')
        return redirect(self.request.path_info)


class INdex(View):
    form_class = EmployeesForm
    initial = {'key': 'value'}
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'all_workers': Employees.objects.all()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('-' * 50)
            # print('form')
            print(form.cleaned_data)
            form.save()
            return redirect('/')
        else:
            print('-' * 50)
            print('не валидна')
            return render(request, self.template_name, {'form': form})
