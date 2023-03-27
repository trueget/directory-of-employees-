from django.urls import path
# from employees.views import index
from .views import (
    INdex,
    AllWorkersListVew,
    OneWorker,
    # search_workers,
    SearchView
)

app_name = 'employees'

urlpatterns = [
    # path('', index, name='index'),
    path('', INdex.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),

    # path('', search_workers,),
    path('all_workers/', AllWorkersListVew.as_view(), name='all_workers'),
    path('one_worker/id=<int:pk>/', OneWorker.as_view(), name='one_worker'),
]