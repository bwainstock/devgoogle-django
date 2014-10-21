# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetstream', '0005_auto_20141018_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='profile_img_url',
            field=models.TextField(default='https://pbs.twimg.com/profile_images/491446558114607104/bgugbG4L.jpeg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweets',
            name='real_name',
            field=models.TextField(default='https://pbs.twimg.com/profile_images/491446558114607104/bgugbG4L.jpeg'),
            preserve_default=False,
        ),
    ]
