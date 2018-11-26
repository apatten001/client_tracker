# Generated by Django 2.1.3 on 2018-11-23 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('Birthday', models.DateField()),
                ('phone_number', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]