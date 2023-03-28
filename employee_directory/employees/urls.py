from django.urls import path
# from employees.views import index
from .views import (
    Index,
    AllWorkersListVew,
    OneWorker,
    AllWorkersListAjaxView
)

app_name = 'employees'

urlpatterns = [
    path('', Index.as_view(), name='index'),

    path('all_workers/', AllWorkersListVew.as_view(), name='all_workers'),
    path('all_workers/ajax/', AllWorkersListAjaxView.as_view(), name='all_workers_ajax'),

    path('one_worker/id=<int:pk>/', OneWorker.as_view(), name='one_worker'),
]
