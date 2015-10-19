# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pubUserAttr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('pubcount', models.IntegerField(default=0)),
                ('uid', models.IntegerField(default=0)),
                ('profileinfo', models.CharField(unique=True, max_length=128)),
                ('authinfo', models.CharField(unique=True, max_length=128)),
                ('subby', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='subUserAttr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('subcount', models.IntegerField(default=0)),
                ('uid', models.IntegerField(default=0)),
                ('profileinfo', models.CharField(unique=True, max_length=128)),
                ('subto', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128)),
                ('isStar', models.IntegerField(default=0)),
                ('friendscount', models.IntegerField(default=0)),
                ('friendslist', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('region', models.CharField(max_length=128)),
                ('subcount', models.IntegerField(default=0)),
                ('pubcount', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
