# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0002_auto_20150921_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='visitas',
            field=models.IntegerField(default=0),
        ),
    ]
