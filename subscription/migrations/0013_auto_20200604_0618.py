# Generated by Django 3.0.6 on 2020-06-04 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0012_auto_20200603_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='amount',
            new_name='amount_paid',
        ),
    ]
