# Generated by Django 2.1.3 on 2018-11-26 11:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_auto_20181125_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='goal_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]