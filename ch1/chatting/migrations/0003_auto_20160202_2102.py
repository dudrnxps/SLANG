# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0002_member_m_mail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Membership',
        ),
    ]