# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliances',
            name='room',
        ),
        migrations.RemoveField(
            model_name='appliances',
            name='wireless',
        ),
        migrations.AddField(
            model_name='roomid',
            name='appliance',
            field=models.ForeignKey(default=1, to='sample.Appliances'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wireless',
            name='appliances',
            field=models.ForeignKey(default=1, to='sample.Appliances'),
            preserve_default=False,
        ),
    ]
