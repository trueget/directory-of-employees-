from django.urls import path
# from employees.views import index
from .views import (
    INdex,
    AllWorkersListVew
)

app_name = 'employees'

urlpatterns = [
    # path('', index, name='index'),
    path('', INdex.as_view(), name='index'),
    path('all_workers/page=<int:page>/', AllWorkersListVew.as_view(paginate_by=500), name='all_workers'),
]