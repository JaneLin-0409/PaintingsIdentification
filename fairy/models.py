from django.db import models


class Page(models.Model):
    diary = models.TextField(verbose_name='日记内容', blank=True)
    time = models.TextField(verbose_name='写作时间', blank=True)
    fell = models.TextField(verbose_name='过后感想', blank=True)
    delete_diary = models.TextField(verbose_name='已删除的日记内容', blank=True)
    count = models.IntegerField(verbose_name='浏览次数', default=0, blank=True)
    creat_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    def __str__(self):
        return str(self.diary)

    class Mata:
        verbose_name = '我的日记表'
        verbose_name_plural = verbose_name

