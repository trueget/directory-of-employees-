from django.db import models

# Create your models here.


class JobTitle(models.TextChoices):
    '''профессии'''
    number_5 = ('OM', 'Ordinary Worker')
    number_4 = ('DP', 'Department Head')
    number_3 = ('MN', 'Manager')
    number_2 = ('DI', 'Director')
    number_1 = ("BG", 'Big Boss')


class Employees(models.Model):
    '''таблица работника'''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(
        choices=JobTitle.choices,
        max_length=2
    )
    salary = models.IntegerField()
    recruitment = models.DateField(auto_now_add=True)
    supervisor = models. ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='boss',
        verbose_name='Руководитель',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['id']
