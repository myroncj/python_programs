# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chips', '0002_auto_20170301_0352'),
    ]

    operations = [
        migrations.CreateModel(
            name='gps',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
    ]
