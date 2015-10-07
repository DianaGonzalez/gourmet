# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255, null=True, blank=True)),
                ('pclav', models.TextField(null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('visitas', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
