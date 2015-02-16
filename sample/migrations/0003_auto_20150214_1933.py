# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20150214_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomid',
            name='appliance',
        ),
        migrations.RemoveField(
            model_name='wireless',
            name='appliances',
        ),
        migrations.AddField(
            model_name='appliances',
            name='roomid',
            field=models.OneToOneField(default=1, to='sample.RoomID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appliances',
            name='wireless',
            field=models.OneToOneField(default=1, to='sample.Wireless'),
            preserve_default=False,
        ),
    ]
