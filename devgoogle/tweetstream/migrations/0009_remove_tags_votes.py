# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetstream', '0008_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='votes',
        ),
    ]
