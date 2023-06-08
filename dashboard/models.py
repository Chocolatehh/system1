from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='分类名称')
    created_at = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

    def __str__(self):
        return self.title


class WenWu(models.Model):
    title = models.CharField(max_length=200, verbose_name='文物名称')
    intro = models.TextField(verbose_name='文物介绍')
    origin_picture = models.ImageField(verbose_name='原图')
    repair_picture = models.ImageField(verbose_name='修复图', upload_to='repair/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    created_at = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

    def __str__(self):
        return self.title