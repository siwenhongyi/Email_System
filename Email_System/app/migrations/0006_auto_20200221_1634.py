# Generated by Django 3.0.3 on 2020-02-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200221_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_head',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
