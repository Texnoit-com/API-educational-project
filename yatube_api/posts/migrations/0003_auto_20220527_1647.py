# Generated by Django 2.2.16 on 2022-05-27 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220527_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date', 'author'), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
