# Generated by Django 3.1 on 2020-09-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCarnet', '0006_auto_20200917_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnet',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]