# Generated by Django 3.1.1 on 2020-09-16 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_user_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
    ]
