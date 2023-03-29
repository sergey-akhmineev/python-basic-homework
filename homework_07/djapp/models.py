from django.db import models


class UserName(models.Model):
    username = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'имя пользователя'
        verbose_name_plural = 'имена пользователей'
        ordering = ['pk']


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    username = models.ForeignKey(UserName, default=name, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}, {self.name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['pk']
