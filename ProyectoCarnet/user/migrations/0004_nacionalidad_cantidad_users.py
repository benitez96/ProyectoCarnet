# Generated by Django 3.1 on 2020-09-28 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200927_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='nacionalidad',
            name='cantidad_users',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
