# Generated by Django 4.1 on 2022-11-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('population', '0004_alter_register_vht_vhtidn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_vht',
            name='VHTIDN',
            field=models.CharField(max_length=50),
        ),
    ]
