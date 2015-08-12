# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedHit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_data', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_path', models.ImageField(upload_to=b'images/%Y/%m/%d')),
                ('url', models.CharField(max_length=150, blank=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.IntegerField(choices=[(1, b'all'), (2, b'General')])),
                ('title', models.CharField(max_length=90)),
                ('slug', models.SlugField()),
                ('teaser_html', models.TextField(editable=False)),
                ('content_html', models.TextField(editable=False)),
                ('tweet_text', models.CharField(max_length=140, editable=False)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('published', models.DateTimeField(null=True, editable=False, blank=True)),
                ('view_count', models.IntegerField(default=0, editable=False)),
                ('author', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
                'get_latest_by': 'published',
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
                ('teaser', models.TextField()),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
                ('published', models.DateTimeField(null=True, blank=True)),
                ('view_count', models.IntegerField(default=0, editable=False)),
                ('author', models.ForeignKey(related_name='revisions', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(related_name='revisions', to='biblion.Post')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(related_name='images', to='biblion.Post'),
        ),
    ]
