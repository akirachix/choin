# Generated by Django 3.2.4 on 2021-11-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadership', '0002_user_is_previously_logged_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedeemableItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rewards/')),
                ('item_name', models.CharField(max_length=50)),
                ('item_value', models.FloatField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('item_in_stock', models.BooleanField(default=True)),
            ],
        ),
    ]