# Generated by Django 4.1 on 2022-11-10 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('population', '0002_report_death_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_death',
            name='Gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='population.register_birth'),
        ),
    ]
