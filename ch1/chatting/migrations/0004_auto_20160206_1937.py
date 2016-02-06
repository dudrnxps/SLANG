# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0003_auto_20160202_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('file_size', models.IntegerField(default=0)),
                ('file_data', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='m_mail',
            new_name='mem_mail',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='m_pass',
            new_name='mem_pass',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='m_id',
            new_name='mem_username',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='m_id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='t_name',
        ),
        migrations.AddField(
            model_name='membership',
            name='mem_username',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='membership_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatting.Membership'),
        ),
        migrations.AddField(
            model_name='file',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatting.Team'),
        ),
    ]