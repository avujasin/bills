# Generated by Django 3.0.6 on 2020-06-04 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_monthlybills_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlybills',
            name='payment_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
