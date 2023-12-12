from django.db import models
from django.conf import settings
# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    surname = models.CharField(max_length=100, verbose_name='Отчество')
    email = models.EmailField(unique=True, verbose_name='Почта')
    comments = models.TextField(verbose_name='Комментарий')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Доктор')


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.surname}'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
