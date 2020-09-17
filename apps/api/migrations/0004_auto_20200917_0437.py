# Generated by Django 3.1.1 on 2020-09-17 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_is_admin'),
        ('api', '0003_auto_20200916_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='api.event')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='sessionattendance',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='sessionattendance',
            name='session',
        ),
        migrations.DeleteModel(
            name='EventAttendance',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.DeleteModel(
            name='SessionAttendance',
        ),
    ]
