# Generated by Django 3.2.7 on 2021-10-28 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bed_capacity', '0011_alter_rumahsakit_kode_lokasi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rumahsakit',
            name='kode_lokasi',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='bed_capacity.wilayah'),
        ),
    ]
