# Generated by Django 4.1 on 2022-11-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('population', '0003_alter_report_death_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_vht',
            name='VHTIDN',
            field=models.CharField(max_length=20),
        ),
    ]