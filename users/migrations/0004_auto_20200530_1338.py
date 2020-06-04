# Generated by Django 3.0.6 on 2020-05-30 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200530_1338'),
        ('users', '0003_remove_tutorprofile_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='is_student',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='cources',
            field=models.ManyToManyField(related_name='interested_students', to='course.Course'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
