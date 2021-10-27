# Generated by Django 3.2.4 on 2021-10-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Leadership'), (2, 'Trainer'), (3, 'Student')], null=True),
        ),
    ]