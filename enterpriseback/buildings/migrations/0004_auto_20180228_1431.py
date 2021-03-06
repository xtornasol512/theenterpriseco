# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-02-28 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_auto_20160824_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='building/'),
        ),
        migrations.AlterField(
            model_name='departmengalery',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(upload_to='building/Departments/'),
        ),
        migrations.AlterField(
            model_name='department',
            name='number_of_apartment',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Apartment Number'),
        ),
        migrations.AlterField(
            model_name='nearbyatraction',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(upload_to='building/NearbyAtraction/'),
        ),
    ]
