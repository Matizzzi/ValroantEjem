# Generated by Django 5.0.7 on 2024-08-03 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_suscripcion_alter_venta_fecha'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Suscripcion',
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 8, 3, 12, 20, 12, 910043)),
        ),
    ]
