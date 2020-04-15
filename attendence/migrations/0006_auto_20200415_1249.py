# Generated by Django 3.0.5 on 2020-04-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0005_auto_20200415_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='day1',
            field=models.CharField(blank=True, choices=[('', ''), ('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='day2',
            field=models.CharField(blank=True, choices=[('', ''), ('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], default='', max_length=10),
        ),
    ]