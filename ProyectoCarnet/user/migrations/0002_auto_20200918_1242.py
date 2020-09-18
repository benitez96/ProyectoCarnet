# Generated by Django 3.1 on 2020-09-18 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCarnet', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='carnet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCarnet.carnet'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCarnet.cedula'),
        ),
    ]