# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20150916_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='submission',
            field=models.OneToOneField(to='ratings.Submission'),
        ),
    ]
