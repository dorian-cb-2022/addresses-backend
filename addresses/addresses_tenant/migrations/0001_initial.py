# Generated by Django 3.2.14 on 2022-07-17 22:26

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(max_length=256)),
                ('latitude', models.DecimalField(decimal_places=7, default=Decimal('0'), max_digits=10)),
            ],
        ),
    ]
