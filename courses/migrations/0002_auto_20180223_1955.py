# Generated by Django 2.0.2 on 2018-02-23 19:55

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='课程详情'),
        ),
    ]
