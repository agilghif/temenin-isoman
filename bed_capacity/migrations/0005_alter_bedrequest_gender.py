# Generated by Django 3.2.7 on 2021-10-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bed_capacity', '0004_alter_bedrequest_rs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedrequest',
            name='gender',
            field=models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], default='L', max_length=1),
        ),
    ]
