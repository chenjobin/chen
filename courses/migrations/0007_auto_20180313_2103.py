# Generated by Django 2.0.2 on 2018-03-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20180313_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.TextField(default='爱奇艺优酷等复制过来时，修改一下height为500，宽度为90%', verbose_name='访问地址'),
        ),
    ]
