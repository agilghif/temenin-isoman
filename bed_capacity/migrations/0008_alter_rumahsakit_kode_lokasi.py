# Generated by Django 3.2.7 on 2021-10-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bed_capacity', '0007_auto_20211028_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rumahsakit',
            name='kode_lokasi',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
