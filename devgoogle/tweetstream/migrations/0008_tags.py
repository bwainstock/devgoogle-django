# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetstream', '0007_auto_20141018_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=140)),
                ('votes', models.IntegerField(default=0)),
                ('tweet', models.ManyToManyField(to='tweetstream.Tweets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
