# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('id', models.IntegerField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomID',
            fields=[
                ('id', models.IntegerField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wireless',
            fields=[
                ('id', models.IntegerField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('address', models.CharField(unique=True, max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='roomid',
            name='wireless',
            field=models.ForeignKey(to='sample.Wireless'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appliances',
            name='room',
            field=models.ForeignKey(to='sample.RoomID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appliances',
            name='wireless',
            field=models.ForeignKey(to='sample.Wireless'),
            preserve_default=True,
        ),
    ]
