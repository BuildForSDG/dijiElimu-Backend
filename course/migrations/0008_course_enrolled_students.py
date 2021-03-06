# Generated by Django 3.0.6 on 2020-06-03 13:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0010_auto_20200603_1221'),
        ('course', '0007_auto_20200603_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrolled_students',
            field=models.ManyToManyField(through='subscription.Subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]
