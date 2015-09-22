# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('filename', models.TextField()),
                ('filetype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code_quality', models.IntegerField(default=0)),
                ('documentation', models.IntegerField(default=0)),
                ('problem_solving', models.IntegerField(default=0)),
                ('effort', models.IntegerField(default=0)),
                ('creativity', models.IntegerField(default=0)),
                ('originality', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('application_date', models.DateTimeField()),
                ('submission_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='submission',
            field=models.ForeignKey(to='ratings.Submission'),
        ),
        migrations.AddField(
            model_name='media',
            name='submission',
            field=models.ForeignKey(to='ratings.Submission'),
        ),
    ]
