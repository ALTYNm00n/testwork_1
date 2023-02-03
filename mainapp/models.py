from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=120,verbose_name='навание')
    description = models.CharField(max_length=120,verbose_name='описание')
    start_date = models.DateField(verbose_name='дата старта ')
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = verbose_name + 'ы'