# Generated by Django 2.2.2 on 2021-09-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary', models.TextField(blank=True, verbose_name='日记内容')),
                ('time', models.TextField(blank=True, verbose_name='写作时间')),
                ('fell', models.TextField(blank=True, verbose_name='过后感想')),
                ('delete_diary', models.TextField(blank=True, verbose_name='已删除的日记内容')),
                ('count', models.IntegerField(blank=True, default=0, verbose_name='浏览次数')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
            ],
        ),
    ]
