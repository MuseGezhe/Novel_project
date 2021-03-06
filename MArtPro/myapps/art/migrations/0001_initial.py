# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('summary', models.CharField(max_length=200, verbose_name='简介')),
                ('content', models.TextField(null=True, verbose_name='内容')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='分类名')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '分类表',
                'db_table': 't_cate',
            },
        ),
        migrations.AddField(
            model_name='art',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art.Category', verbose_name='分类'),
        ),
    ]
