from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.template.loader import render_to_string

from django.views import View

from .models import Employees
from .forms import EmployeesForm

from django.db.models import Q


# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class Index(View):
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
            return redirect('all_workers')
        else:
            return render(request, self.template_name, {'form': form})


class AllWorkersListVew(ListView):
    '''список всех работников'''
    model = Employees
    template_name = 'all_workers.html'
    paginate_by = 500

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Employees.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
        else:
            sort_order = self.request.GET.get('sort', 'id')
            # object_list = Employees.objects.all()
            object_list = Employees.objects.order_by(sort_order)

        return object_list


class AllWorkersListAjaxView(AllWorkersListVew):
    template_name = 'sorted_list.html'

    def get_queryset(self):
        sort_order = self.request.GET.get('sort', '-id')
        print('-'*70)
        print(sort_order)
        return Employees.objects.order_by(sort_order)

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            html = render_to_string(self.template_name, context)
            return HttpResponse(html)
        else:
            return super().render_to_response(context, **response_kwargs)


class OneWorker(ListView):
    '''один работник с подчиненными и руководителем'''
    model = Employees
    template_name = 'one_worker.html'
    context_object_name = 'one_worker'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worker'] = Employees.objects.get(id=self.kwargs['pk'])
        return context
