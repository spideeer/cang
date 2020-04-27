# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CargoInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cargo_ID', models.IntegerField(max_length=30)),
                ('cargo_name', models.CharField(max_length=100)),
                ('amount', models.IntegerField(max_length=10)),
                ('in_price', models.IntegerField(max_length=10)),
                ('out_price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cargoinfo',
            name='userinfo',
            field=models.ForeignKey(to='moon.UserInfo'),
        ),
    ]
