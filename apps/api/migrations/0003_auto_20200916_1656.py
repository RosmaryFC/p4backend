# Generated by Django 3.1.1 on 2020-09-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200916_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(),
        ),
    ]
