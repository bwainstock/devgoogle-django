# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetstream', '0006_auto_20141018_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweets',
            old_name='profile_img_url',
            new_name='profile_image_url',
        ),
    ]
