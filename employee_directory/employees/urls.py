from django.urls import path
# from employees.views import index
from .views import INdex

app_name = 'employees'

urlpatterns = [
    # path('', index, name='index'),
    path('', INdex.as_view(), name='index')
]