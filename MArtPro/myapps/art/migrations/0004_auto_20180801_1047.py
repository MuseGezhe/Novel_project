# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 02:47
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0003_art_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='art',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='art/images/', verbose_name='封面'),
        ),
    ]