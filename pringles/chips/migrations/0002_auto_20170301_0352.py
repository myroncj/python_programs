# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chips1',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('t', models.IntegerField()),
                ('s', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Graph',
        ),
    ]
