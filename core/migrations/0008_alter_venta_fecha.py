# Generated by Django 5.0.7 on 2024-08-03 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 8, 3, 13, 56, 19, 782909)),
        ),
    ]
