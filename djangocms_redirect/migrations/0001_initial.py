# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        #('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_path', models.CharField(db_index=True, help_text="This should be an absolute path, excluding the domain name. Example: '/events/search/'.", max_length=200, verbose_name='redirect from')),
                ('new_path', models.CharField(blank=True, help_text="This can be either an absolute path (as above) or a full URL starting with 'http://'.", max_length=200, verbose_name='redirect to')),
                ('response_code', models.CharField(choices=[('301', '301'), ('302', '302')], default='301', help_text='This is the http response code returned if a destination is specified. If no destination is specified the response code will be 410.', max_length=3, verbose_name='response code')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='site')),
            ],
            options={
                'ordering': ('old_path',),
                'db_table': 'django_redirect',
                'verbose_name': 'redirect',
                'verbose_name_plural': 'redirects',
            },
        ),
        migrations.AlterUniqueTogether(
            name='redirect',
            unique_together=set([('site', 'old_path')]),
        ),
    ]
