# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_auto_20180731_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='cover',
            field=models.ImageField(null=True, upload_to='art/images/', verbose_name='封面'),
        ),
    ]