# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetstream', '0003_auto_20141018_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
