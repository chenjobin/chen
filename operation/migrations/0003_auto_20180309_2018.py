# Generated by Django 2.0.2 on 2018-03-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180222_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='comments',
            field=models.CharField(max_length=200, verbose_name='笔记'),
        ),
    ]
