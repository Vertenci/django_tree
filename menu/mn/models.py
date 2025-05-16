from django.db import models
from django.urls import reverse


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Название меню")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE, verbose_name="Меню")
    title = models.CharField(max_length=100, verbose_name="Название")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children',
                               on_delete=models.CASCADE, verbose_name="Родительский элемент")

    def get_absolute_url(self):
        return reverse('item', kwargs={'title': self.title})

    def __str__(self):
        return self.title
