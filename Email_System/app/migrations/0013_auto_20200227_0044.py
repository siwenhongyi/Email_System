# Generated by Django 3.0.3 on 2020-02-26 16:44

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('app', '0012_auto_20200227_0026'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mail',
            new_name='Mymail',
        ),
    ]
