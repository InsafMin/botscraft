from django.db import models
from django.urls import reverse


class Crafter(models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Контент")
    token = models.CharField(max_length=255, verbose_name="Токен")
    logo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Логотип")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('request', kwargs={'request_id': self.pk})

    class Meta:
        verbose_name = 'Запрос на создание бота'
        verbose_name_plural = 'Запросы на создание бота'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class User(models.Model):
    objects = None
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Логотип")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
