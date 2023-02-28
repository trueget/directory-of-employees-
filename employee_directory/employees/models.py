from django.db import models

# Create your models here.


class JobTitle(models.TextChoices):
    '''профессии'''
    number_5 = (5, 'number_5')
    number_4 = (4, 'number_4')
    number_3 = (3, 'number_3')
    number_2 = (2, 'number_2')
    number_1 = (1, 'number_1')


class Employees(models.Model):
    '''таблица работника'''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sur_name = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.IntegerField(
        choices=JobTitle.choices,
        default=JobTitle.number_5
    )
    salary = models.IntegerField()
    recruitment = models.DateField(auto_now_add=True)
    supervisor = models.OneToOneField(
        'self',
        on_delete=models.PROTECT,
        related_name='boss'
    )
    subordinates = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='workers'
    )
