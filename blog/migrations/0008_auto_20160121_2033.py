# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160121_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d'),
        ),
    ]
